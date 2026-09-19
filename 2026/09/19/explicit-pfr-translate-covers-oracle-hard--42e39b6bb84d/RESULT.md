# Explicit PFR translate covers are oracle-hard even below doubling two

## Statement

Let \(m\ge 2\), let
\[
G=\mathbb F_2^{2m}=H\oplus W,
\qquad \dim H=\dim W=m,
\]
and, for every nonzero \(z\in W\), define
\[
A_z:=H\cup\{z\}.
\]
Then
\[
|A_z|=2^m+1,
\qquad
A_z+A_z=H\cup(z+H),
\qquad
K(A_z)=\frac{2^{m+1}}{2^m+1}<2.
\]
Moreover, among subspaces \(V\le G\) with \(|V|\le |A_z|\), the minimum number of translates needed to cover \(A_z\) is exactly two: the two translates \(H\) and \(z+H\) suffice, while a one-translate cover would force a subspace containing \(H\) and \(z\), hence size at least \(2^{m+1}>|A_z|\).

Consider the same oracle model used in algorithmic Polynomial Freiman--Ruzsa (PFR) results: an algorithm receives independent uniform samples from \(A_z\) and point-membership access to \(A_z\). Strengthen the algorithm by additionally giving it a basis of \(H\) for free. Suppose it must output a subspace \(V\le G\) and at most \(L\) translation representatives \(t_1,\ldots,t_L\) such that
\[
|V|\le |A_z|
\quad\text{and}\quad
A_z\subseteq\bigcup_{i=1}^L(t_i+V).
\]
If it uses at most \(s\) uniform samples and \(q<2^m-1\) membership queries, then for uniformly random \(z\in W\setminus\{0\}\) its success probability is at most
\[
\boxed{
\frac{s}{2^m+1}
+\frac{q}{2^m-1}
+\frac{L^2}{2^m-1-q}.
}
\]
Consequently, if \(L^2\le(2^m-1)/12\), every randomized algorithm that succeeds with probability at least \(2/3\) for every \(A_z\) uses more than \((2^m-1)/6\) oracle interactions in the worst case. In particular, for every fixed \(L\), and more generally for every \(L=\operatorname{poly}(m)\), explicit translate-cover recovery requires
\[
2^{\Omega(m)}=2^{\Omega(n)}
\]
interactions for ambient dimension \(n=2m\), despite \(K(A_z)<2\), despite the existence of an optimal two-coset cover, and even when the covering subspace \(H\) itself is already known.

Thus the recent polynomial-time algorithmic PFR theorems, which output a basis of a subspace whose polynomially many translates are guaranteed to cover \(A\), cannot in this oracle model be strengthened in general to output the covering translate representatives themselves with polynomial complexity.

## Structural lemma: one output covers only \(L^2\) hidden outliers

Fix a subspace \(V\le G\) with \(|V|\le2^m+1\), and suppose \(L\) translates of \(V\) cover \(H\). Since \(|V|\) is a power of two,
\[
\dim V\le m.
\]
Put \(U=V\cap H\) and \(h=\dim U\). Every coset of \(V\) intersects \(H\), if at all, in a coset of \(U\), and therefore in exactly \(2^h\) points. Covering all \(2^m\) points of \(H\) by at most \(L\) such cosets requires
\[
2^m\le L2^h,
\qquad\text{so}\qquad
2^{m-h}\le L.
\]
Let \(\pi:G\to G/H\) be the quotient map. Then
\[
\dim \pi(V)
=\dim V-\dim(V\cap H)
\le m-h,
\]
so every projected coset \(\pi(t_i+V)\) contains at most
\[
2^{\dim\pi(V)}\le2^{m-h}\le L
\]
quotient classes. Hence
\[
\left|\pi\!\left(\bigcup_{i=1}^L(t_i+V)\right)\right|\le L^2.
\]
Distinct elements of the chosen complement \(W\) lie in distinct \(H\)-cosets. Therefore any fixed output that covers \(H\) can also cover at most \(L^2\) possible choices of the hidden outlier \(z\in W\setminus\{0\}\).

## Oracle lower bound

Let \(M=2^m-1\) and choose \(z\) uniformly from \(W\setminus\{0\}\).

A uniform sample from \(A_z\) equals the exceptional point \(z\) with probability \(1/(2^m+1)\). Conditioned on not seeing \(z\), the sample is uniform on \(H\), and hence contains no information about which nonzero \(z\in W\) was chosen. By a union bound, \(s\) samples reveal \(z\) with probability at most \(s/(2^m+1)\).

For membership queries, every point of \(H\) has answer one for all \(z\), every point outside \(H\cup W\) has answer zero for all \(z\), and a query \(w\in W\setminus\{0\}\) has answer one exactly when \(w=z\). Up to the first positive answer, an adaptive deterministic strategy therefore tests at most \(q\) candidate values of \(z\). Conditional on the sample transcript not revealing \(z\), the probability of such a membership hit is at most \(q/M\).

If neither access mechanism hits \(z\), then after at most \(q\) candidate exclusions the hidden point is uniform over at least \(M-q\) possibilities. By the structural lemma, the algorithm's fixed output can be valid for at most \(L^2\) of them. Thus the residual success probability is at most \(L^2/(M-q)\). Conditioning on the internal randomness gives the same bound for randomized algorithms, yielding
\[
\Pr[\mathrm{success}]
\le
\frac{s}{2^m+1}+\frac{q}{M}+\frac{L^2}{M-q}.
\]

For the stated constant, assume \(s+q\le M/6\) and \(L^2\le M/12\). Then
\[
\frac{s}{2^m+1}+\frac{q}{M}\le\frac{s+q}{M}\le\frac16,
\]
and, since \(q\le M/6\),
\[
\frac{L^2}{M-q}\le\frac{M/12}{5M/6}=\frac1{10}.
\]
The total is at most \(4/15<2/3\), contradicting worst-case success at least \(2/3\). Hence more than \(M/6\) interactions are necessary.

## Context

Recent algorithmic PFR work asks, from uniform-sample and membership-oracle access to a small-doubling set \(A\subseteq\mathbb F_2^n\), for an explicit basis of a subspace \(V\) with \(|V|\le|A|\) such that \(A\) is coverable by polynomially many translates of \(V\). The September 2026 polynomial-time result outputs exactly such a basis in \(\operatorname{poly}(n,K)\) time. Earlier 2025--2026 algorithmic PFR results use the same output convention: the subspace is explicit, while the translating set is guaranteed to exist. A robust 2026 variant likewise outputs subspaces and bounds the covering number \(\mathcal N_V(A)\).

The family above shows that this output convention marks a genuine oracle-complexity boundary. For \(K<2\), any \(K^{O(1)}\) bound on the number of covering translates is an absolute constant, yet listing representatives of such a cover can require exponentially many oracle interactions. The obstruction is not computational difficulty in finding the structured subspace: that subspace is supplied for free. It is the information cost of locating a rare exceptional coset.

## Limitations

The lower bound concerns explicit lists of translation representatives. It does not contradict algorithms that output only a subspace together with an existential covering-number guarantee, nor algorithms given a stronger oracle capable of returning an element from a requested occupied coset. The hard family uses a single rare outlier and the exact PFR size condition \(|V|\le|A|\); it does not rule out efficient witnesses under additional density, regularity, or alternative output representations. The originality claim is to the best of our knowledge; because the proof is short and uses a deliberately simple hard family, folklore risk remains material.

## Reproducibility

`artifacts/verify_cover_barrier.py` is a standalone Python script. It verifies the exact small-doubling identity for \(m=1,\ldots,8\), enumerates all relevant subspaces for ambient dimensions up to six, and checks the dimension/projection inequalities behind the \(L^2\) structural bound. Its recorded output is in `artifacts/verification.txt`. These finite checks are supplementary; the theorem is proved analytically above.

## References

1. S. Arunachalam, A. Dutt, S. Grewal, A. Gupte, *Marton's conjecture in polynomial time*, arXiv:2609.20771 (2026). https://arxiv.org/abs/2609.20771
2. D. Castro-Silva, J. Briët, S. Arunachalam, A. Dutt, T. Gur, *An algorithmic Polynomial Freiman-Ruzsa theorem*, arXiv:2604.04547 (2026). https://arxiv.org/abs/2604.04547
3. S. Arunachalam, D. Castro-Silva, A. Dutt, T. Gur, *Classical and Quantum Polynomial Freiman-Ruzsa Algorithms*, ITCS 2026. https://doi.org/10.4230/LIPIcs.ITCS.2026.11
4. C. Peng, *Robust Polynomial Freiman-Ruzsa from Corrupted Set Observations*, arXiv:2608.00451 (2026). https://arxiv.org/abs/2608.00451
