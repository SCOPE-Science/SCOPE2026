# Sharp logarithmic power growth of the canonical Schreier shift

## Finding
For each real number \(1\le p<\infty\), let \(S_p\) denote the real or complex \(p\)-convexified first Schreier space, and let the canonical right shift \(R\) satisfy \(Re_j=e_{j+1}\). For every integer \(n\ge0\),
\[
\boxed{\frac{H_{n+2}-1}{\log 2}\le\|R^n\|_{S_p\to S_p}^{p}\le\left\lceil\log_2(n+2)\right\rceil,}
\]
where \(H_m=\sum_{j=1}^{m}j^{-1}\). Consequently,
\[
\boxed{\|R^n\|_{S_p\to S_p}^{p}=\frac{\log n}{\log 2}+O(1)\quad(n\to\infty).}
\]
The leading coefficient \(1/\log2\) is sharp, uniformly in the choice of real or complex scalars and for each fixed \(p\). Every finitely supported vector has an eventually constant orbit norm, whereas the set of vectors with unbounded orbit norms is residual.

## Assumptions and scope
Let \(\mathcal S_1\) be the family of finite subsets \(F\) of \(\mathbb N=\{1,2,\ldots\}\) satisfying \(F=\varnothing\) or \(|F|\le\min F\). Define \(S_p\) as the completion of the finitely supported scalar sequences for
\[
\|x\|_{S_p}=\sup_{F\in\mathcal S_1}\left(\sum_{j\in F}|x_j|^p\right)^{1/p}.
\]
The shift \(R\) acts by the coefficient rule \((Rx)_1=0\) and \((Rx)_{j+1}=x_j\); boundedness on the completion follows from the estimate below with \(n=1\). All conclusions concern this fixed canonical basis, not arbitrary rearrangements of Schreier families.

## Proof
**Upper bound.** Fix a finitely supported \(x\) and an admissible nonempty set \(F\) in the image. Pull back its intersection with the support of \(R^nx\) by subtracting \(n\), obtaining an ordered nonempty set \(B=\{b_1<\cdots<b_s\}\). Put \(m=b_1\). Since \(F\) is Schreier admissible, \(s\le m+n\). Partition the ordered entries of \(B\) successively into blocks of up to \(m,2m,4m,\ldots\) entries. The first element of the block with nominal capacity \(2^rm\) is at least \(m+\sum_{t=0}^{r-1}2^tm=2^rm\), because the positive integer entries are strictly increasing. Thus every block is itself Schreier admissible, even if the last block is incomplete. No more than
\[
L=\left\lceil\log_2(1+s/m)\right\rceil\le\left\lceil\log_2(n+2)\right\rceil
\]
blocks are needed. Summing their disjoint contributions gives \(\sum_{j\in B}|x_j|^p\le L\|x\|_{S_p}^p\), and taking both suprema proves the stated upper bound. The argument also establishes bounded extension of each power from finitely supported vectors.

**Lower bound.** Define a finitely supported vector \(u^{(n)}\) by \(u^{(n)}_j=(j+1)^{-1/p}\) for \(1\le j\le n+1\), zero otherwise. If \(E\) is Schreier admissible with \(m=\min E\), monotonicity of the coefficients and \(|E|\le m\) imply
\[
\sum_{j\in E}|u^{(n)}_j|^p\le\sum_{j=m}^{2m-1}\frac1{j+1}\le\int_m^{2m}\frac{dt}{t}=\log2.
\]
Here the integral comparison uses \(1/(j+1)\le\int_j^{j+1}dt/t\) for every positive integer \(j\). Therefore \(\|u^{(n)}\|_{S_p}^p\le\log2\). After shifting \(n\) times, the set \(\{n+1,\ldots,2n+1\}\) has cardinality and minimum both equal to \(n+1\), so
\[
\|R^nu^{(n)}\|_{S_p}^p\ge\sum_{j=1}^{n+1}\frac1{j+1}=H_{n+2}-1.
\]
The norm ratio gives the claimed lower bound. Since \(H_{n+2}=\log n+O(1)\), and the upper ceiling is \(\log n/\log2+O(1)\), these two bounds establish the sharp asymptotic.

**Orbit contrast.** If \(x\) has finite support \(E\), then for all sufficiently large \(n\) the shifted support \(E+n\) is Schreier admissible. Thus \(\|R^nx\|_{S_p}=\big(\sum_{j\in E}|x_j|^p\big)^{1/p}\) eventually; in particular all finitely supported vectors have bounded orbits. Their span is dense. On the other hand, \(\|R^n\|\to\infty\). By the uniform boundedness theorem and the Baire-category argument (the closed sets \(\{x:\sup_n\|R^nx\|\le M\}\) each have empty interior), the vectors with unbounded orbit norm form a dense \(G_\delta\) subset of \(S_p\).

## Verification
The analytic bounds use only finite admissible-set partitions and an exact harmonic witness. The accompanying `check.py` evaluates 10,657 finite consistency diagnostics: rational partial-harmonic estimates, block-capacity coverage, and compatibility of the explicit two-sided bounds. These are ancillary tests, not a substitute for the proofs of the uniform inequalities or asymptotic.

## Relationship to prior work
Gulgowski and Sawicki (2026) develop combinatorial Banach spaces and compactness criteria, with primary MSC2020 classification 46B50. Bird and Laustsen (2010), Section 3.15–3.17, previously characterize which right coordinate shifts are bounded on \(p\)-Schreier spaces; for a translation by \(n\), their general method supplies a polynomial upper bound in \(n\), not the stated logarithmic asymptotic with its optimal constant. The present argument exploits the specific additive translation and geometric Schreier block structure. This is not a new proof of either paper's existing general classification.

## Limitations
No exact closed form for \(\|R^n\|\) at every finite \(n\) is claimed; the explicit bounds leave a uniformly bounded gap in their \(p\)-th powers. The theorem concerns the first Schreier family and its standard \(p\)-convexifications, not higher Schreier families, noncanonical permutations, or arbitrary spreading families. Literature searches and the comparison of accessible primary texts cannot exclude an equivalent formulation in unexamined prior literature. Independent scientific validation has not been performed.

## References
1. J. Gulgowski and P. Sawicki, *Compactness in Combinatorial Banach Spaces and Beyond*, arXiv:2610.09810v1 (first publicly submitted October 7, 2026), https://arxiv.org/html/2610.09810v1 .
2. A. Bird and N. J. Laustsen, *An amalgamation of the Banach spaces associated with James and Schreier, Part I*, Section 3, available in open text at https://eprints.lancs.ac.uk/id/eprint/39691/4/BirdLaustsen_stdlatex.pdf .
