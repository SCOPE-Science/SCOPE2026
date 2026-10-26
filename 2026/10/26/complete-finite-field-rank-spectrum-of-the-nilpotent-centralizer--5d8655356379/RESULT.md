# Complete finite-field rank spectrum of the nilpotent centralizer of consecutive Jordan blocks

## Finding

Let \(m\ge2\), let \(q\) be any prime power, and fix the nilpotent matrix \(B=J_m(0)\oplus J_{m-1}(0)\) over \(\mathbb F_q\). Write \(\mathcal N_B=\{X:XB=BX,\ X\text{ nilpotent}\}\), and define its ordinary rank-generating polynomial \(P_{m,q}(z)=\sum_{X\in\mathcal N_B}z^{\operatorname{rank}_{\mathbb F_q}X}\). The following finite recursions determine **every rank multiplicity** with no restriction on characteristic.

For integers \(\ell\ge1\), set
\[
H_\ell(z)=1+(q-1)\sum_{r=1}^{\ell-1}q^{r-1}z^r,\quad
U_q=(q^2-1)(q^2-q),\quad V_q=(q-1)(q+1)^2.
\]
Starting with \(G_0(z)=1\), define
\[
G_\ell(z)=G_{\ell-1}(z)+U_qq^{4(\ell-1)}z^{2\ell}
+V_qq^{3(\ell-1)}z^\ell H_\ell(z).
\]
Then the exact answer is
\[
\boxed{P_{m,q}(z)=G_{m-2}(z)
+q^{4m-7}(q-1)^2z^{2m-2}
+(2q^2-q-1)q^{3m-6}z^{m-1}H_{m-1}(z).}
\]
In particular, \(|\mathcal N_B|=q^{4m-5}\), the number of regular nilpotent matrices in \(\mathcal N_B\) is exactly \((q-1)^2q^{4m-7}\), and the fraction of such matrices is \((1-q^{-1})^2\), independent of \(m\). The regular-nilpotent stratum is geometrically isomorphic to \((\mathbb G_m)^2\times\mathbb A^{4m-7}\); the whole nilpotent centralizer is an affine space \(\mathbb A^{4m-5}\).

## Assumptions and scope

Here \(J_s(0)\) denotes one nilpotent Jordan block of size \(s\), and \(\operatorname{rank}\) is ordinary rank on the full \((2m-1)\)-dimensional vector space, not rank over a truncated polynomial ring. The case \(m=2\) is included. The geometric assertions concern the reduced affine varieties parametrized by the displayed coefficients, over any field (after base extension where needed). The finite-field formula holds for all prime powers, including fields of characteristic two.

## Proof

Regard the underlying module as \(M=R_m\oplus R_{m-1}\), with \(R_s=k[t]/(t^s)\), and let \(B\) act as multiplication by \(t\). Every endomorphism commuting with \(B\) has a unique block description
\[
X(u,v)=(a(t)u+t b(t)v,\ c(t)u+d(t)v),
\]
where \(a\in R_m\), \(b,c\in R_{m-1}\), and \(d\in R_{m-1}\), with the expression for \(c(t)u\) interpreted modulo \(t^{m-1}\). On the semisimple quotient of the endomorphism algebra, the two diagonal constant terms are the only coordinates; the two indecomposable summands have distinct lengths. Thus \(X\) is nilpotent exactly when these two constants vanish. Equivalently write
\[
a=t\alpha,\qquad d=t\delta,
\]
with \(\alpha,b,c\in R_{m-1}\) and \(\delta\in R_{m-2}\). Indeed \(X^2(M)\subseteq tM\), so \(X^{2m}=0\) in this form; conversely a nonzero diagonal constant survives a quotient simple module and prohibits nilpotence. This supplies exactly \((m-1)+(m-1)+(m-1)+(m-2)=4m-5\) free coefficients.

Put \(\ell=m-1\), so \(R=R_\ell\). The image of \(X\) lies in \(tR_m\oplus R_\ell\). Dividing the first component by \(t\), then factoring the source by \(t^\ell R_m\) in its first summand, identifies the induced map with the \(R\)-linear endomorphism
\[
T=\begin{pmatrix}\alpha&b\\c&t\delta\end{pmatrix}:R^2\longrightarrow R^2.
\]
Both the first division and quotient preserve the underlying \(k\)-dimension of the image, hence \(\operatorname{rank}_kX=\operatorname{rank}_kT\). Conversely every such \(T\) arises uniquely. This reduces the problem to computing the \(k\)-rank distribution of \(2\times2\) matrices over \(R\) whose lower-right entry is divisible by \(t\).

First consider unrestricted \(2\times2\) matrices over \(R_\ell\), and denote their rank polynomial by \(G_\ell\). Reduction modulo \(t\) has rank two in precisely \(U_q=|\mathrm{GL}_2(\mathbb F_q)|\) cases and rank one in precisely \(V_q=(q-1)(q+1)^2\) cases; exactly one residue matrix has rank zero. Every residue matrix has \(q^{4(\ell-1)}\) lifts. A rank-two residue produces full \(k\)-rank \(2\ell\). For each fixed rank-one residue, invertible elementary row and column operations bring the lifted matrix to \(\operatorname{diag}(1,h)\), and its Schur complement \(h\) ranges uniformly over \(tR_\ell\), with exactly \(q^{3(\ell-1)}\) lifts for each \(h\). Its rank is \(\ell+\operatorname{rank}_k(h:R_\ell\to R_\ell)\), while the rank-generating sum over \(h\in tR_\ell\) is precisely \(H_\ell(z)\). Finally, a matrix with zero residue is uniquely \(tT'\), for arbitrary \(T'\in M_2(R_{\ell-1})\), and has the same \(k\)-rank as \(T'\). These disjoint cases prove the displayed recurrence for \(G_\ell\) and the base case \(G_0=1\).

For the constrained matrix \(T\), its residue is \(\begin{psmallmatrix}a_0&b_0\\c_0&0\end{psmallmatrix}\), of which exactly \(q(q-1)^2\) are invertible, \(2q^2-q-1\) have rank one, and one is zero. The rank-two stratum lifts as before. For every fixed rank-one residue, choose a nonzero pivot among \(a_0,b_0,c_0\). The Schur complement is uniform over \(tR_\ell\): with \(a_0\ne0\), vary the lower-right entry; with \(a_0=0,b_0\ne0\), vary the lower-left entry; with \(a_0=b_0=0,c_0\ne0\), vary the upper-right entry. In each case the chosen free entry ranges over \(tR_\ell\), and elementary operations give \(\operatorname{diag}(1,h)\). There are \(q^{3(\ell-1)}\) lifts per \(h\). The zero-residue stratum is \(tT'\) with *unrestricted* \(T'\in M_2(R_{\ell-1})\), contributing \(G_{\ell-1}\). Summation yields the formula for \(P_{m,q}\).

Finally \(X\) has rank \(2m-2\) exactly when \(T\) is invertible over \(R\), equivalently \(b_0c_0\ne0\). Such a nilpotent operator on dimension \(2m-1\) has exactly one Jordan block, so this is precisely the regular-nilpotent stratum. The two nonzero constants \(b_0,c_0\) are independent, and all other \(4m-7\) coordinates are arbitrary, proving the geometric description and the count. Evaluating the rank polynomial at \(z=1\) recovers \(q^{4m-5}\).

## Verification

Run `python3 verify.py` using Python 3 and no additional dependencies. The verifier directly constructs all matrices commuting with \(J_m(0)\oplus J_{m-1}(0)\) in six finite settings, calculates ordinary ranks by independent finite-field Gaussian elimination, and compares the resulting histogram with the recurrences. The settings include \((m,q)=(2,2),(3,2),(4,2),(3,3),(2,4),(3,4)\), covering both prime fields and a nonprime finite field. The coefficient count, regularity criterion, and selected literal commutation and nilpotence checks are also verified. The terminal marker is `VERIFY_OK_CONSECUTIVE_JORDAN_RANK_SPECTRUM`. These finite checks are corroboration, not an infinite proof.

## Relationship to prior work

The existence and maximal nilpotency index of regular nilpotents in centralizers of almost-rectangular Jordan types follows from prior studies such as Oblak (2007). Work on generic nilpotent commuting orbits and the irreducible nilpotent centralizer includes Basili and Iarrobino (2007) and Košir and Oblak (2007). Hua (2023) treats canonical forms of two-block commuting nilpotent pairs with unequal lengths. Bogdanić and collaborators (2022 preprint, 2024 journal) classify *possible* Jordan structures for two **equal** block lengths. The statement assessed here is instead the **finite-field multiplicity of every ordinary rank** for all consecutive block sizes, including its explicit rank-polynomial recursion and universal regular-nilpotent density. In the inspected treatments no such all-rank finite-field count was located; older or differently indexed literature could still contain an equivalent formula.

## Limitations

This is a rank distribution, not the complete Jordan-partition distribution: multiple distinct nilpotent Jordan types may share a rank. It assumes exactly two consecutive Jordan blocks; neither arbitrary partitions nor arbitrary finite chain rings are treated. No independent mathematical audit or exhaustive literature-priority certification has been performed. The relation to the stronger canonical-form results remains a relevant priority risk.

## References

- P. Oblak, *The upper bound for the index of nilpotency for a matrix commuting with a given nilpotent matrix*, arXiv:math/0701561 (first posted 19 January 2007), https://arxiv.org/abs/math/0701561.
- R. Basili and A. Iarrobino, *Pairs of commuting nilpotent matrices, and Hilbert function*, arXiv:0709.2304 (2007), https://arxiv.org/abs/0709.2304.
- T. Košir and P. Oblak, *On pairs of commuting nilpotent matrices*, arXiv:0712.2813 (2007), https://arxiv.org/abs/0712.2813.
- J. Hua, *Canonical forms for a class of pairs of commuting nilpotent matrices under simultaneous similarity*, arXiv:2305.00176 (2023), https://arxiv.org/abs/2305.00176.
- D. Bogdanić et al., *Jordan structures of nilpotent matrices in the centralizer of a nilpotent matrix with two Jordan blocks of the same size*, arXiv:2212.08425 (2022), https://arxiv.org/abs/2212.08425.
