# Every kernel rank occurs for base-power periodic sequences

## Finding
Fix integers \(k\ge 2\) and \(t\ge 1\). Among all one-sided sequences on arbitrary finite output alphabets whose **least positive period is exactly** \(k^t\), the possible numbers of distinct sequences in their \(k\)-kernels are **exactly**
\[
\left\{t+2,t+3,\ldots,\frac{k^{t+1}-1}{k-1}\right\}.
\]
In particular this natural noncoprime family has no gaps (no missing automatic-sequence ranks) between its sharp endpoints. The result concerns the **cardinality of the kernel**, not the vector-space dimension of a regular sequence and not the state complexity for most-significant-digit-first automata.

## Assumptions and scope
A sequence is a map \(s:\mathbb N_0\to\Gamma\), where \(\Gamma\) is an arbitrary *finite* alphabet, allowed to depend on the sequence. The least period \(P\) is the smallest positive integer satisfying \(s(n+P)=s(n)\) for every \(n\ge0\). Its base-\(k\) kernel is
\[
K_k(s)=\{(s(k^e n+j))_{n\ge0}:e\ge0,\ 0\le j<k^e\},
\]
and its kernel rank is \(\rho_k(s)=|K_k(s)|\). Two kernel elements coincide only if their infinite output sequences agree pointwise. Relabeling the output symbols bijectively preserves this cardinality. The theorem asserts existence over finite alphabets of unrestricted size; it does **not** assert existence over a fixed binary output alphabet.

Write \(B_t=\sum_{e=0}^{t}k^e\). The proof gives sharp universal bounds \(t+2\le\rho_k(s)\le B_t\) and witnesses for every integer between them.

## Proof
**1. Bounds.** If \(s\) has period \(k^t\), then every kernel sequence at depth \(e=t\) is constant: \(s(k^t n+j)=s(j)\). All deeper kernel sequences are constant too. There are at most \(k^e\) depth-\(e\) nodes, giving \(\rho_k(s)\le B_t\). A period word using \(k^t\) distinct symbols attains \(B_t\): no two nodes at any level coincide, as every shallower node is nonconstant and all their disjoint residue subsequences contain distinct symbols.

For the lower bound, at least one kernel element at depth \(t-1\) is nonconstant; otherwise \(s\) would have period dividing \(k^{t-1}\). Follow its ancestor chain from depth zero. Every one of these \(t\) nodes is nonconstant. They are pairwise different: if a nonconstant node repeated at a greater depth along the chain, the intervening nonempty sequence of decimation maps \(u(n)\mapsto u(kn+j)\) would send that node back to itself. Iterating those maps would produce nonconstant nodes at arbitrarily great depths, contradicting the depth-\(t\) constancy. Finally \(s\) uses at least two distinct output letters (its least period exceeds one), and each occurs as a constant depth-\(t\) kernel element. Hence \(\rho_k(s)\ge t+2\).

**2. Interleaving lemma.** Suppose \(m\) sequences \(u_0,\ldots,u_{m-1}\), where \(1\le m\le k\), each have least period \(k^{t-1}\), kernel ranks \(q_0,\ldots,q_{m-1}\), and contain a shared output symbol \(0\). Relabel their other symbols so that their nonzero alphabets are pairwise disjoint; for the remaining \(k-m\) positions use the constant-zero sequence. Define
\[
s(kn+j)=\begin{cases}u_j(n),&0\le j<m,\\0,&m\le j<k.\end{cases}
\]
Its least period is \(k^t\). Indeed, choose a nonzero symbol of \(u_0\); it occurs only in positions congruent to zero modulo \(k\), so every period is divisible by \(k\). After dividing a period by \(k\), the quotient is a period of \(u_0\), hence a multiple of \(k^{t-1}\). The converse period \(k^t\) is immediate.

The depth-zero element \(s\) is different from all its children and descendants because it has a strictly longer least period. The descendants below the children are exactly their kernels, together with the zero constant. Nonzero alphabet disjointness shows that two descendants of different children can coincide only when both are the constant-zero sequence. Each child kernel contains zero because it contains every constant letter at depth \(t-1\). Consequently,
\[
\rho_k(s)=2+\sum_{j=0}^{m-1}(q_j-1).
\tag{1}
\]
This equality is exact, not merely a bound.

**3. Base cases.** For \(t=1\), a word of least period \(k\) has kernel rank \(1+c\), where \(c\) is the number of distinct letters in its period. Every \(2\le c\le k\) is attained by placing a symbol that occurs just once at the first position and distributing the remaining \(c-1\) symbols over the other positions. Thus the full rank interval is \([3,k+1]\).

For \((k,t)=(2,2)\), the four least-period-four words `0001`, `0102`, `0012`, `0123` (with different numerals denoting different symbols) have respective kernel ranks \(4,5,6,7\); these exhaust the required interval. Their ranks are obtained directly by enumerating the root, two depth-one decimations, and constant depth-two decimations.

**4. Induction.** Assume that for exponent \(t-1\) every rank in \([L,U]\) occurs, where \(L=t+1\) and \(U=B_{t-1}\). The interleaving lemma, with \(m\) active children and any chosen \(q_j\in[L,U]\), realizes every integer in
\[
I_m=[2+mt,\ 2+m(U-1)],\qquad 1\le m\le k.
\]
The sums fill these intervals without gaps because each summand independently varies through consecutive integers. If \(k\ge3,t\ge2\), or \(k=2,t\ge3\), then \(U\ge2t\), so consecutive \(I_m\) overlap or touch. Their union is therefore the whole interval
\[
[t+2,\ 2+k(U-1)].
\]
To obtain the final \(k-1\) ranks, take \(k\) children of maximal rank \(U\), each represented by a word using \(k^{t-1}\) distinct symbols, and initially identify one chosen letter of each child as the common zero while leaving all other letters distinct across children. Equation (1) gives rank \(2+k(U-1)\). For any \(1\le h\le k-1\), replace the zero letter in each of the first \(h\) children by a fresh private letter. Every child still has kernel rank \(U\), and the resulting union of child kernels has exactly \(h\) additional distinct constant elements (at least one zero remains). Its parent thus has rank \(2+k(U-1)+h\). These are precisely all the remaining integers up to
\[
2+k(U-1)+(k-1)=1+kU=B_t.
\]
This completes the induction and the proof. \(\square\)

## Verification
The supplied standalone `verify.py` computes kernel ranks exactly from finite period words: at each depth through \(t\) it forms every residue subsequence and reduces it to its least period. It checks a recursively generated witness for **every** permitted rank for the parameter pairs \((k,t)=(2,1),\ldots,(2,5),(3,1),\ldots,(3,3),(4,1),(4,2)\), totaling 168 witnesses. It independently enumerates all canonical set-partition patterns of the period for the parameter pairs \((2,1),(2,2),(2,3),(3,1),(3,2)\), checks the exact least periods and attainable rank sets, and examines 25,285 primitive patterns. The actual result was `VERIFY_OK constructed_witnesses=168 primitive_partition_census=25285`. These finite tests are consistency checks; the proof of the general theorem is the induction above.

Reproduction: run `python3 verify.py` with a standard Python 3 interpreter and no third-party packages.

## Relationship to prior work
Kreczman, Prigioniero, Rowland, and Stipulanti, *Magic Numbers in Periodic Sequences* (arXiv:2304.03268; first version publicly submitted 2023-04-06), define these same automatic-sequence kernel ranks, prove a general maximum bound, and characterize attainable ranks for period \(\ell\) **coprime** to the base. Their conclusion (Section 6) explicitly leaves noncoprime parameters for future investigation. Our theorem addresses the specific noncoprime family \(\ell=k^t\) and supplies the whole spectrum, including a constructive no-gap result not entailed by their maximum bound.

Wieb Bosma, *Complexity of Periodic Sequences* (2019), analyzes periodic binary sequences and formulates Conjecture 12 giving, when its odd factor is one, the lower bound \(t+2\) for binary outputs in base two. The general lower-bound proof here covers that special lower bound but the main added conclusion is the **entire rank spectrum with output alphabet allowed to grow**; it does not settle Bosma's binary-alphabet rank-spectrum questions. Bosma's discussion of interleaving and upper bounds does not establish this full unrestricted-alphabet interval theorem.

## Limitations
This proof does not address periods having both base-sharing and coprime factors, fixed-size (especially binary) output alphabets, \(k\)-regular vector-space ranks, or distinct ranks of most-significant-digit-first minimal automata. The originality comparison is based on the inspected works and available searches, not a claim of comprehensive priority certification; an equivalent result under different terminology may exist. No independent audit has been performed.

## References
1. S. Kreczman, L. Prigioniero, E. Rowland, and M. Stipulanti, *Magic Numbers in Periodic Sequences*, arXiv:2304.03268 (2023), https://arxiv.org/abs/2304.03268 ; freely available full text https://ericrowland.github.io/papers/Magic_numbers_in_periodic_sequences.pdf .
2. W. Bosma, *Complexity of Periodic Sequences* (2019), https://www.math.ru.nl/~bosma/pubs/periodic.pdf .
