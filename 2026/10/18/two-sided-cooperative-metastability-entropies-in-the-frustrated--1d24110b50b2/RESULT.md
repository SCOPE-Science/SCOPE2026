# Two-sided cooperative metastability entropies in the frustrated Ising ring

## Finding
For every integer \(N\ge8\), coupling \(J>0\), and frustration ratio \(0<\kappa<1\), consider the periodic Ising Hamiltonian
\[
H(s)=-J\sum_{i=0}^{N-1}s_i s_{i+1}+J\kappa\sum_{i=0}^{N-1}s_i s_{i+2},\qquad s_i\in\{-1,+1\},
\]
with indices modulo \(N\). Call a configuration weakly \(r\)-stable if no simultaneous flip of a nonempty set of at most \(r\) **distinct** spins strictly lowers \(H\). Let \(A_N^{(r)}(\kappa)\) count these configurations, retaining vertex labels and both global spin signs. A spin domain is a maximal cyclic interval of equal spins; a uniform configuration has no domain walls.

Every weakly one-stable configuration has either no walls or all domains of length at least two. Among these, **the complete weak two-spin-stable classification** is:

* If \(0<\kappa<1/2\), the two uniform configurations and precisely the nonuniform configurations whose domains all have length at least three.
* If \(\kappa=1/2\), exactly the weakly one-stable configurations, equivalently all global ground states.
* If \(1/2<\kappa<1\), precisely the nonuniform configurations whose domains all have lengths between two and five inclusive; the uniform configurations are then excluded.

Consequently, with \(\varphi=(1+\sqrt5)/2\), and with \(\lambda_-\) and \(\lambda_+\) the unique real roots greater than one of
\[
\lambda_-^3-\lambda_-^2-1=0,\qquad
\lambda_+^5-\lambda_+^3-\lambda_+^2-\lambda_+-1=0,
\]
we have
\[
\lim_{N\to\infty}\frac1N\log A_N^{(1)}(\kappa)=\log\varphi,
\quad
\lim_{N\to\infty}\frac1N\log A_N^{(2)}(\kappa)=
\begin{cases}
\log\lambda_-&0<\kappa<1/2,\\
\log\varphi&\kappa=1/2,\\
\log\lambda_+&1/2<\kappa<1.
\end{cases}
\]
Numerically, the three two-spin entropy densities in increasing coupling order are \(0.382245085840\ldots\), \(0.481211825060\ldots\), and \(0.427981530066\ldots\). Both off-critical bases are smaller than \(\varphi\): outside the multiphase point, the fraction of one-spin minima surviving all pair flips decays exponentially in \(N\), whereas at the multiphase point it equals one exactly.

## Assumptions and scope
The model is a *classical* zero-field Ising ring with ferromagnetic nearest-neighbor and antiferromagnetic next-nearest-neighbor couplings. Weak stability excludes strictly energy-lowering moves but allows neutral moves; the result does not count absorbing states for dynamics that permit neutral moves. The two flipped sites need not be adjacent. The length bound \(N\ge8\) avoids accidental coincidences in local periodic neighborhoods. The coupling interval is strict at \(\kappa=0\) and \(\kappa=1\). No claim is made about the distribution reached by a stochastic quench.

## Proof
**Wall reduction.** Put \(t_i=s_i s_{i+1}\in\{-1,+1\}\), \(w_i=(1-t_i)/2\), \(W=\sum_i w_i\), and \(P=\sum_i w_i w_{i+1}\). Expanding \(s_i s_{i+2}=t_i t_{i+1}\) gives the exact identity
\[
H(s)=-J(1-\kappa)N+J(2-4\kappa)W+4J\kappa P.\tag{1}
\]
The spin-wall parity constraint is that \(W\) is even. Two walls separated by one bond enclose a spin domain of length one.

**Single flips.** Flipping spin \(i\) changes its energy by
\[
\frac{\Delta_i H}{2J}=t_{i-1}+t_i-\kappa(t_{i-2}t_{i-1}+t_i t_{i+1}).\tag{2}
\]
If \(t_{i-1}=t_i=-1\), then \(\Delta_iH\le-4J(1-\kappa)<0\). Conversely, if no two negative \(t\)'s are adjacent, then (2) is strictly positive when both central \(t\)'s are positive and nonnegative when exactly one is negative. Thus weak one-stability is exactly the absence of adjacent walls, or \(P=0\).

**All two-site flips.** For sites separated by at least three in cyclic graph distance, the pair increment is the sum of the two nonnegative single-site increments, because no Hamiltonian interaction joins the selected sites. For sites at distance two, the correction to that sum is \(4J\kappa s_i s_{i+2}\). If this factor is positive, the pair increment is nonnegative. If it is negative, precisely one of \(t_i,t_{i+1}\) is negative. Assume \(t_i=-1,t_{i+1}=1\) (the reversed case is symmetric). Absence of adjacent walls forces \(t_{i-1}=1\). If \(t_{i+2}=1\), then (2) yields \(\Delta_{i+2}H\ge4J\), so the pair increment is at least \(4J(1-\kappa)>0\). If \(t_{i+2}=-1\), no adjacent walls forces \(t_{i+3}=1\); then (2) gives exactly \(\Delta_{i+2}H=4J\kappa\), which cancels the negative correction, leaving \(\Delta_iH\ge0\). Thus only **adjacent** pairs can add an instability (distance-two pairs can be energy-neutral).

For the flip of sites \(i,i+1\), only the bonds \(t_{i-1}=a\) and \(t_{i+1}=c\) reverse; write \(u=t_{i-2},b=t_i,v=t_{i+2}\). Directly from (1),
\[
\frac{\Delta_{i,i+1}H}{2J}=a+c-\kappa(au+ab+bc+cv).\tag{3}
\]
Under the no-adjacent-negative-wall restriction, all five-sign cases in (3) are nonnegative for \(0<\kappa<1\), except precisely these two possible cases:
\[
(u,a,b,c,v)=(+,-,+,-,+):\quad\Delta_{i,i+1}H=4J(2\kappa-1),
\]
\[
(u,a,b,c,v)=(+,+,+,+,+):\quad\Delta_{i,i+1}H=4J(1-2\kappa).
\]
For completeness, if \(a,c\) have opposite signs, the sum in parentheses in (3) is nonpositive, so the increment is nonnegative; if both are negative, the no-adjacency hypothesis forces the first displayed pattern; if both are positive, the sum is at most four, attaining four only at the second displayed pattern, and otherwise at most two, giving an increment at least \(4J(1-\kappa)>0\). The first pattern is exactly a domain of length two; the second is exactly five consecutive wall-free bonds. This proves the classification. At \(\kappa=1/2\), (1) simplifies to \(H=-JN/2+2JP\), so all one-spin-stable configurations are indeed global ground states.

**Counting.** For a set \(D\) of allowed domain lengths, put \(F_D(z)=\sum_{\ell\in D}z^\ell\). A nonuniform cyclic spin word has an even, positive number \(2r\) of spin domains. Marking a wall and then removing the marking gives the ordinary generating function for vertex-labeled cyclic spin words
\[
C_D(z)=\sum_{N\ge1}C_{D,N}z^N=-z\frac{d}{dz}\log(1-F_D(z)^2).
\tag{4}
\]
Indeed, an ordered list of \(2r\) domain lengths summing to \(N\) admits \(2N/(2r)=N/r\) distinct choices of initial spin and site origin, after correcting the overcount from wall-rooting. The three allowed sets are \(D_- =\{3,4,\ldots\}\), \(D_0=\{2,3,\ldots\}\), and \(D_+=\{2,3,4,5\}\). Thus, for all \(N\ge8\),
\[
A_N^{(1)}=2+[z^N]C_{D_0}(z),\quad
A_N^{(2)}=\begin{cases}
2+[z^N]C_{D_-}(z),&0<\kappa<1/2,\\
2+[z^N]C_{D_0}(z),&\kappa=1/2,\\
[z^N]C_{D_+}(z),&1/2<\kappa<1.
\end{cases}\tag{5}
\]
In each case \(F_D\) has positive consecutive-degree coefficients, and \(F_D(r)=1\) has a unique solution \(r\in(0,1)\); (4) has a simple dominant pole at \(r\), with no competing same-modulus poles. It follows by coefficient extraction that \(C_{D,N}\sim r^{-N}\). Substituting the three explicit \(F_D\)'s gives the stated algebraic bases and entropy densities. Strict inequalities \(\lambda_\pm<\varphi\) follow because the two off-critical length sets are strict subsets of \(D_0\). This also proves the exponential survivor-fraction statement.

## Verification
Run `python verify.py` using Python 3 standard library. The program checks the Hamiltonian's wall representation, exhaustively enumerates all labeled spin configurations and all one- and two-site flips for lengths eight through fourteen at three representative coupling ratios, and compares with independently counted cyclic domain compositions. It additionally checks near-boundary rational couplings at shorter lengths and computes the three characteristic roots. Successful finite checks are supplementary evidence; equations (1)–(5), the local case analysis, and the generating-function singularity argument prove the infinite-size statements.

## Relationship to prior work
Dhar, Shastry, and Dasgupta established and studied extensive ground-state degeneracy at the one-dimensional axial-next-nearest-neighbor Ising multiphase point, including golden-mean ground-state entropy, and investigated constrained Kawasaki dynamics. Their convention uses a staggered-spin representation; the multiphase ground-state words correspond to the domain restriction \(D_0\) here. That equilibrium entropy and the critical-point degeneracy are **prior results**, not claimed as new. Their inspected manuscript does not give the full off-critical weak one-/two-spin local-minimum classification, the arbitrary-pair condition, or both off-critical two-spin entropy roots. Ismail and Hassan studied metastability with random fields and reported finite-chain single-spin energy minima; their available abstract does not settle this simultaneous-pair theorem. An inaccessible full text cannot be declared inapplicable based on an abstract, so its possible stronger results are an originality risk. The present assertion is confined to the complete off-critical cooperative-stability classification and its exact entropies.

## Limitations
The result does not treat \(\kappa\le0\), \(\kappa\ge1\), a nonzero field, unequal/disordered couplings, higher-dimensional lattices, strict stability, moves flipping three or more spins, or stochastic selection probabilities. It gives an exponential count of mathematically stable states, not a relaxation-time or dynamical trapping probability. The paper by Ismail and Hassan was not inspected in full; hidden equivalent coverage and work indexed under alternative terminology remain possible.

## References
1. A. Dhar, B. S. Shastry, C. Dasgupta, *Equilibrium and dynamical properties of the ANNNI chain at the multiphase point*, arXiv:cond-mat/0004207v1 (first public arXiv version 13 April 2000), https://arxiv.org/pdf/cond-mat/0004207.
2. G. Ismail and S. Hassan, *Metastability of Ising spin chains with nearest-neighbour and next-nearest-neighbour interactions in random fields*, Chinese Physics 11 (2002), 948–954, doi:10.1088/1009-1963/11/9/318.
