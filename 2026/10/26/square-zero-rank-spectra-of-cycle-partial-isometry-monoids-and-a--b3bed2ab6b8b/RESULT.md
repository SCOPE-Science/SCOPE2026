# Square-zero rarity and conditional rank for cycle partial isometries

## Finding

Let \(C_n\), \(n\ge3\), be the graph cycle with its geodesic distance, and let \(f\) be uniform over the **distinct partial isometries** of \(C_n\), including the empty map. Write \(s_n\) for the number satisfying \(f^2=0\), and let \(R_n\) be the domain size conditional on \(f^2=0\). Set \(\lambda=(1+\sqrt5)/2\) and \(\beta=7^{1/4}\). The counts satisfy
\[
s_n=\begin{cases}
n3^{(n-1)/2}+O(n\lambda^n+n^2),&n\text{ odd},\\
(2n/3+1)3^{n/2}+O(n\beta^n+n^2),&n\text{ even}.
\end{cases}
\]
Consequently \(\Pr(f^2=0)\) is asymptotic to \((\sqrt3/2)^n/(2\sqrt3)\) for odd \(n\), and to \((\sqrt3/2)^n/3\) for even \(n\).

More precisely, define a law \(\nu_n\) on ranks as follows. Use \(\operatorname{Bin}((n-1)/2,2/3)\) for odd \(n\). For even \(n\), use the mixture of \(\operatorname{Bin}(n/2,2/3)\) and \(\operatorname{Bin}(n/2-1,2/3)\) with respective weights \(3(n+2)/(4n+6)\) and \(n/(4n+6)\). Then
\[
d_{\mathrm{TV}}(\mathcal L(R_n),\nu_n)=
\begin{cases}
O((\lambda/\sqrt3)^n),&n\text{ odd},\\
O((\beta/\sqrt3)^n),&n\text{ even}.
\end{cases}
\]
In particular \((R_n-n/3)/(\sqrt n/3)\) converges in law to a standard normal and \(R_n/n\) converges in probability to \(1/3\).

## Assumptions and scope

A partial isometry preserves distances on its domain and is therefore injective. Zero is the empty partial map. A map has square zero exactly when its domain and image are disjoint. Uniformity is over maps, not global extensions or domains. All asymptotics are taken separately along the indicated parities. Total variation is half the sum of absolute differences of probability masses.

## Proof

Every partial isometry is a restriction of a dihedral permutation [1, Lemma 1.1]. For fixed \(g\), count restriction domains \(A\) satisfying \(A\cap g(A)=\varnothing\), giving weight \(z^{|A|}\). On a fixed point the factor is 1, on a transposition it is \(1+2z\), and on a permutation orbit of length \(d\ge3\) it is the independence polynomial of a cycle of length \(d\). These follow by making an independent choice on each permutation orbit: a vertex cannot be chosen together with its successor.

Let \(F_n(z)\) be the rank polynomial of distinct square-zero maps; counting extension pairs initially counts some maps more than once. Two distinct global permutations agree only on the fixed points of their nonidentity quotient, hence on at most two vertices. A singleton restriction has exactly two extensions, and a rank-two restriction has two only when its domain is antipodal. The empty map has \(2n\) extensions. Thus the difference between extension-pair counts and map counts is nonnegative at every rank, with total at most \((2n-1)+n^2+n^2/2=O(n^2)\): for antipodal domains there are at most \((n/2)^2\) domain/image pair choices with two bijections each. This bound suffices without a coefficient-by-coefficient duplication formula.

The dominant extension types are all reflections and, in even size, the half-turn. Write \(M_n(z)\) for their combined rank polynomial (counting pairs before identifying duplicates). For odd size each of the \(n\) reflections has one fixed point, giving
\[
M_n(z)=n(1+2z)^{(n-1)/2}.
\]
For even size the \(n/2\) fixed-point-free reflections and the half-turn each give \((1+2z)^{n/2}\), whereas the other \(n/2\) reflections give \((1+2z)^{n/2-1}\). Therefore
\[
M_n(z)=(n/2+1)(1+2z)^{n/2}+(n/2)(1+2z)^{n/2-1}.
\]

For a nonidentity rotation other than an even half-turn, all its permutation orbits have a common length \(d\ge3\) dividing \(n\). The independent-set count on a \(d\)-cycle is \(L_d=\lambda^d+(-1/\lambda)^d\). Indeed, at weight one the trace of the two-state transition matrix \(\bigl(\begin{smallmatrix}1&1\\1&0\end{smallmatrix}\bigr)^d\) counts all labeled cyclic binary words with no adjacent ones, and its two eigenvalues are \(\lambda\) and \(-1/\lambda\). If \(d\) is odd, then \(L_d<\lambda^d\). If \(d\) is even, then \(d\ge4\) and \(L_d^{1/d}=\lambda(1+\lambda^{-2d})^{1/d}\le L_4^{1/4}=\beta\), since \(d^{-1}\log(1+\lambda^{-2d})\) decreases in positive \(d\). Each rotation contributes \(L_d^{n/d}\) extension pairs. Including the identity, the omitted rotations contribute \(O(n\lambda^n)\) in odd size and \(O(n\beta^n)\) in even size. In particular, with \(\gamma=\lambda\) or \(\beta\) according to parity,
\[
E_n:=\sum_k |[z^k](F_n-M_n)|=O(n\gamma^n+n^2).
\]
This follows by adding the nonnegative mass of omitted pairs and the nonnegative mass of duplicates removed. At \(z=1\) this proves the counts; dividing by the total monoid size \(n2^{n+1}-\frac{(-1)^n+5}{4}n^2-2n+1\sim2n2^n\) from [1, Theorem 1.4] gives the stated rarity constants.

Put \(m_n=M_n(1)\). The sum of the absolute coefficient differences between \(F_n/s_n\) and \(M_n/m_n\) is at most \(E_n/m_n+|s_n-m_n|/m_n\le2E_n/m_n\); this uses that the coefficients of \(F_n\) are nonnegative. Since \(m_n\) is of order \(n(\sqrt3)^n\), this proves the exponential total-variation bounds. Normalizing \(M_n\) gives exactly the stated binomial laws and weights. Every binomial component has mean \(n/3+O(1)\) and variance \(n/9+O(1)\); the binomial central limit theorem applies to each, hence to their mixture, and total variation transfers the statement to \(R_n\). This also gives convergence of \(R_n/n\) in probability.

## Relationship to prior work

The dihedral-extension theorem and monoid size are due to Fernandes and Paulista [1]. The earlier general bounded-nilpotency enumerator [2], specialized to exponent two, gives the exact square-zero rank polynomial for \(n\ge4\), including the reflection term and the duplication corrections; that exact polynomial is **not** claimed here. The contribution concerns the asymptotic conditional law: the aggregate weight of all longer rotation orbits and repeat representations is uniformly small compared with the reflection and half-turn terms. Keeping the even half-turn in the dominant law allows an exponentially accurate approximation to the full rank distribution. The distinct later law for unrestricted nilpotent partial isometries [3] conditions on a different event and has a different limiting rank density and Gaussian variance constant.

## Limitations

The total-variation error is absolute, not a relative estimate for the probability of an individual extreme rank. The argument is special to square zero, not arbitrary powers. The priority comparison is limited to the inspected sources.

## References

1. V. H. Fernandes and T. Paulista, *On the monoid of partial isometries of a cycle graph*, Turkish Journal of Mathematics 47 (2023), 1746–1760, [arXiv:2205.02196](https://arxiv.org/abs/2205.02196), Lemma 1.1 and Theorem 1.4.
2. *Rank and nilpotency-index enumerators for partial isometries of a cycle*, [Resultary, 2026-10-12](https://github.com/Resultary/2026/tree/main/2026/10/12/SCOPE-rank-and-nilpotency-index-enumerators-for-partial-isometries-of--32e0cfa664d8), Finding, specialization to exponent two.
3. *Nilpotent rank spectra and a binomial law for cycle partial isometries*, [Resultary, 2026-11-08](https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-nilpotent-rank-spectra-and-a-binomial-law-for-cycle-partial-isom--6fca557893ec), Finding.
