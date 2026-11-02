# Exact four-erasure logical-support spectrum of a \([[20,11,4]]\) stabilizer code

## Finding
For the explicitly published twenty-qubit \([[20,11,4]]\) stabilizer code of Dzoba (arXiv:2610.24025v1), let \(S\) be its rank-nine binary symplectic stabilizer, \(N(S)\) its Pauli normalizer, and \(E\subseteq\{0,\ldots,19\}\) an erased set. Define the *supported logical dimension* \(\ell(E)\) as the binary dimension of the vector space of Pauli operators supported inside \(E\) and commuting with \(S\), modulo those in \(S\) supported inside \(E\). Global Pauli phases are ignored.

Among all \(\binom{20}{4}=4845\) four-qubit erasure sets, the exact histogram is
\[
\boxed{\left(\#\{E:|E|=4,\ell(E)=d\}\right)_{d=0,1,2}=(3840,970,35).}
\]
No four-erasure set has larger supported logical dimension. In each of the 35 two-dimensional cases, all supported logical Pauli classes mutually commute: the three nonidentity classes comprise an isotropic two-dimensional logical subspace. Thus precisely 1005 four-qubit erasure patterns are uncorrectable, and 3840 remain exactly correctable. Conditioned on four uniformly random erased qubits, the correctability probability is
\[
\boxed{\frac{3840}{4845}=\frac{256}{323}.}
\]
All sets of size at most three are correctable; every set of size at least five is uncorrectable. Consequently the exact success probability under independent per-qubit erasure probability \(p\in[0,1]\) is
\[
\boxed{P_{\mathrm{succ}}(p)=\sum_{j=0}^{3}\binom{20}{j}p^j(1-p)^{20-j}+3840p^4(1-p)^{16}.}
\]

## Assumptions and scope
The code is precisely the nine-generator Pauli stabilizer listed in `erasure_census.cpp` and `verify_local.py`, copied in the same order from the source paper's released `quantum/q20_11_4_paulis.txt`. Qubits are indexed \(0\) through \(19\). A set \(E\) is correctable if *arbitrary* Pauli errors supported on \(E\) can be distinguished up to stabilizer equivalence, equivalently the Knill–Laflamme criterion for erasure of known positions. This is a worst-case erasure criterion, not a claim about a particular decoder or a depolarizing channel. No claims are made about all \([[20,11,4]]\) codes.

## Proof
**Linear-algebra reduction.** Disregarding phases, Pauli words of length 20 form \(\mathbb F_2^{40}\), with \(X\)-part and \(Z\)-part, and commutation given by the binary symplectic form. The 9 generators span \(S\) of rank 9. Write each as \((x_i,z_i)\), \(1\le i\le9\). The commutator syndrome of a single \(X\) on coordinate \(j\) is the column \((z_{1j},\ldots,z_{9j})\); for a single \(Z\), it is \((x_{1j},\ldots,x_{9j})\). For each four-set \(E\), let \(H_E\) be the 9-by-8 binary matrix formed from these eight syndrome columns.

The local centralizer is precisely the kernel of \(H_E\), of dimension \(8-\operatorname{rank}(H_E)\). The source's stabilizer has minimum nonidentity Pauli weight 12; this is independently confirmed by exhaustive enumeration of all \(2^9=512\) stabilizer combinations. Hence no nonidentity stabilizer is supported on any four-set, so
\[
\ell(E)=8-\operatorname{rank}_{\mathbb F_2}(H_E).
\]
By the stabilizer erasure-correction criterion, \(E\) is correctable exactly when \(\ell(E)=0\).

**Complete exact rank census.** `erasure_census.cpp` reconstructs the nine generators from Pauli symbols, checks their independence and pairwise commutation, reproduces the published stabilizer-weight distribution, and uses binary integer Gaussian elimination. It checks *every* one of the \(4845\) four-coordinate sets. The ranks \(8,7,6\) occur exactly \(3840,970,35\) times; no smaller rank occurs. For the 35 rank-six cases, the independent verifier `verify_local.py` enumerates all \(4^4\) local Pauli operators on each erased set and tests each operator against all nine stabilizers by the symplectic commutator. There are precisely three nonidentity commuting local normalizer elements on each of the 35 cases, and all pairs among them commute. The full local enumeration independently reproduces the \(3840,970,35\) dimension counts. In particular the total number of weight-four logical operators is
\[
970\cdot1+35\cdot3=1075,
\]
matching the weight-four count reported in the source paper but additionally resolving the previously aggregated count into its support multiplicities.

**Other erasure sizes and success probability.** The rank census verifies every set of at most three coordinates is correctable. On any five-set, the local Pauli vector space has binary dimension ten, while at most nine independent stabilizer commutation constraints apply; hence it has a nonzero centralizer vector. Because the minimum stabilizer weight is 12, that vector cannot be a nonidentity stabilizer. Thus every five-set is uncorrectable, and uncorrectability is monotone under enlarging an erased set. Combining these observations with the exact four-set census yields the displayed independent-erasure probability polynomial, with no sampling or asymptotic approximation.

## Verification
Compile `erasure_census.cpp` with a conforming C++17 compiler (`g++ -O3 -std=c++17 erasure_census.cpp -o erasure_census`) and run `./erasure_census`. It enumerates all \(2^{20}\) erasure patterns, computes local syndrome and stabilizer-restriction ranks with exact bit operations, and prints `FOUR_ERASURE_KERNEL_HIST 0:3840 1:970 2:35 ...` followed by `ERASURE_CENSUS_OK`. Run `python3 verify_local.py` using the Python standard library. Its separately implemented Pauli-by-Pauli enumeration of every four-set reports the same histogram and confirms all 35 double-logical cases commute, ending `LOCAL_ENUMERATION_OK`. The latter also reconstructs the 512 stabilizers independently and checks their known weight distribution. Both checkers use only the nine published generators; no optimization output or third-party data file is required.

## Relationship to prior work
Dzoba's October 16, 2026 source publishes the optimal-parameter \([[20,11,4]]\) code, all nine Pauli generators, the stabilizer-weight spectrum \(\{0{:}1,12{:}50,14{:}220,16{:}195,18{:}20,20{:}26\}\), and the **aggregate** count of 1075 weight-four logical operators. Those known facts do not determine how many distinct four-coordinate supports are affected: several different logical operators may have the same support. The present result isolates precisely 1005 distinct failing supports, distinguishes the 970 one-logical cases from the 35 commuting two-logical cases, and obtains the exact random-erasure recovery curve. The general stabilizer erasure criterion and binary symplectic method are classical; the new ingredient claimed here is the complete concrete local-support incidence census, not that general criterion.

## Limitations
This is a complete finite computation for one published code, not a classification of all equivalent or optimal stabilizer codes. The spectrum is independently reproduced by two arithmetic implementations, but no separate human audit of code or publication priority has occurred. The four-set spectrum is not a new minimum-distance claim. The erasure probability assumes independently erased, *known* coordinate positions and exact correctability, not an approximate decoder or an unknown-error model.

## References
1. C. Dzoba, *New lower bounds for binary constant-weight codes from prescribed-automorphism search, and two quantum codes meeting their upper bounds*, arXiv:2610.24025v1 (October 16, 2026), https://arxiv.org/html/2610.24025v1; explicit generators in https://arxiv.org/src/2610.24025v1/anc/quantum/q20_11_4_paulis.txt.
2. A. R. Calderbank, E. M. Rains, P. W. Shor, and N. J. A. Sloane, *Quantum error correction via codes over GF(4)*, IEEE Transactions on Information Theory 44 (1998), 1369–1387. General stabilizer/symplectic framework.
