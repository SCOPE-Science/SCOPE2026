# Sharp Cartier nilpotence on characteristic-two Serre-type maximal curves

## Finding
Let \(k\) be an algebraically closed field of characteristic \(2\), let \(n\geq3\) be odd, and put \(m=(2^n+1)/3\). On the smooth projective curve \(X_n\) with affine model \(y^4+y=x^m\), the Cartier operator \(\mathcal C\) on \(H^0(X_n,\Omega^1)\) satisfies
\[
\boxed{\mathcal C^n=0,\qquad \mathcal C^{n-1}\ne0.}
\]
Thus its exact nilpotency index is \(n\). More precisely, with \(\omega_0=x^{(m-3)/2}y\,dx\), one has \(\mathcal C^{n-1}(\omega_0)=dx\). For every odd \(n\geq5\), the independent differential \(\omega_2=x^{(m-5)/2}y\,dx\) satisfies \(\mathcal C^{n-1}(\omega_2)=x^2\,dx\), so \(\operatorname{rank}(\mathcal C^{n-1})\geq2\).

The proof also identifies a natural indexing of a basis of regular differentials as an *antipodal transversal*: modulo \(M=2^n+1\), at most one of \(s\) and \(-s\) indexes a regular basis differential; the unique pair for which neither does is \(\{m,2m\}\). This explains nilpotence by a half-turn under inverse doubling.

## Assumptions and scope
The field is algebraically closed of characteristic \(2\); no restriction on coefficients other than the displayed model is needed. The integer \(n\) is odd and at least \(3\). The curve is the smooth projective normalization of the affine equation, rather than its possibly singular plane compactification. Its genus is \(g=3(m-1)/2=2^{n-1}-1\). Nilpotency is understood for the semilinear Cartier endomorphism of the \(g\)-dimensional space of global regular differentials. The two explicit images give lower bounds for the final nonzero Cartier rank, not an asserted formula for that rank for all \(n\).

## Proof
**Regular differential basis.** Because \(m\) is odd, the degree-four Artin–Schreier extension \(k(x,y)/k(x)\) has a single pole above infinity and is totally ramified there, with pole orders \(v_\infty(x)=-4\), \(v_\infty(y)=-m\). Its different exponent is \(3(m+1)\). Riemann–Hurwitz gives \(2g-2=-8+3(m+1)=3m-5\). Since the affine equation has derivative \(1\) in \(y\), it is smooth affine and \(dx\) has neither zeros nor poles there, so \(\operatorname{div}(dx)=(3m-5)P_\infty\). Distinct monomials \(x^iy^j\), \(i\geq0\), \(0\leq j\leq3\), have distinct pole orders \(4i+mj\); consequently the regular differential basis is
\[
B=\{\omega_{i,j}=x^iy^j\,dx:i\geq0,\ 0\leq j\leq3,\ 4i+mj\leq3m-5\}.
\]
In particular \(j\leq2\) for every basis element.

**The modular index.** Set \(M=3m=2^n+1\), and index \(\omega_{i,j}\) by \(s=4(i+1)+mj\in\{1,\ldots,M-1\}\). Since \(m\equiv3\pmod4\), the set of indices is exactly
\[
S=\{4,8,\ldots,M-1\}\ \cup\ \{m+4,m+8,\ldots,M-2\}\ \cup\ \{2m+4,2m+8,\ldots,M-3\},
\]
where an interval with lower endpoint exceeding its upper endpoint is empty. The three progressions have residues \(0,3,2\pmod4\), respectively. Their total cardinality is \(g=(M-3)/2\).

If \(s\equiv0\pmod4\), then \(M-s\equiv1\pmod4\) and is absent. If \(s\equiv3\pmod4\), then \(s\geq m+4\), so \(M-s\leq2m-4\), below the allowed residue-two progression. If \(s\equiv2\pmod4\), then \(s\geq2m+4\), so \(M-s\leq m-4\), below the allowed residue-three progression. Therefore \(S\cap(M-S)=\varnothing\). There are \((M-1)/2\) antipodal pairs and \(|S|=(M-3)/2\), leaving exactly one entirely missing pair. Both \(m\) and \(2m\) are absent, so that pair is \(\{m,2m\}\).

**Cartier as inverse doubling.** From \(y=(y^2)^2+x^m\) and the characteristic-two Cartier identities \(\mathcal C(f^2\eta)=f\mathcal C(\eta)\), \(\mathcal C(x^{2a+1}dx)=x^a dx\), and \(\mathcal C(x^{2a}dx)=0\), one obtains, for every basis element,
\[
\begin{aligned}
\mathcal C(\omega_{i,0})&=\begin{cases}\omega_{(i-1)/2,0},&i\text{ odd},\\0,&i\text{ even},\end{cases}\\
\mathcal C(\omega_{i,1})&=\begin{cases}\omega_{(i+m-1)/2,0},&i\text{ even},\\\omega_{(i-1)/2,2},&i\text{ odd},\end{cases}\\
\mathcal C(\omega_{i,2})&=\begin{cases}\omega_{(i-1)/2,1},&i\text{ odd},\\0,&i\text{ even}.\end{cases}
\end{aligned}
\]
All displayed nonzero outputs are in \(B\). Define \(\Phi(s)=s/2\) for even \(s\), and \(\Phi(s)=(s+M)/2\) for odd \(s\). The formulas say that whenever \(\mathcal C(\omega_{i,j})\ne0\), its index is \(\Phi(s)\). When the Cartier image vanishes, \(\Phi(s)\notin S\) (for even \(i\) with \(j=0\), the index lies in the residue-two class below \(2m+4\); for even \(i\) with \(j=2\), it is \(1\pmod4\)). Thus all surviving Cartier trajectories are exactly the trajectories of \(\Phi\) that stay inside \(S\).

Modulo \(M\), \(\Phi(s)\equiv2^{-1}s\), and because \(2^n\equiv-1\pmod M\), one has \(\Phi^n(s)\equiv-s\pmod M\). Any nonzero \(n\)-fold Cartier image of a basis differential would require both \(s\) and \(M-s\) to lie in \(S\), contradicting the antipodal property. Hence \(\mathcal C^n=0\) on the entire space.

**Sharpness and two longest chains.** For \(\omega_0=x^{(m-3)/2}y\,dx\), the even integer \((m-3)/2\) yields
\[
\mathcal C(\omega_0)=x^{(3m-5)/4}\,dx=x^{2^{n-2}-1}\,dx.
\]
Repeated application of \(\mathcal C(x^{2^r-1}dx)=x^{2^{r-1}-1}dx\) for \(r\geq1\) gives \(\mathcal C^{n-1}(\omega_0)=dx\ne0\).

For \(n\geq5\), put \(h=(m-3)/4\), so \(h\equiv2\pmod4\). The differential \(\omega_2=x^{2h-1}y\,dx\) has successive Cartier images
\[
 x^{h-1}y^2\,dx,\quad x^{(h-2)/2}y\,dx,\quad x^{3\cdot2^{n-4}-1}\,dx.
\]
A further \(n-4\) Cartier applications lower the last exponent to \(2\), giving \(\mathcal C^{n-1}(\omega_2)=x^2dx\). Because \(dx\) and \(x^2dx\) are distinct basis elements, \(\operatorname{rank}(\mathcal C^{n-1})\geq2\) when \(n\geq5\). This completes the proof.

## Verification
The standalone standard-library program `verify.py` enumerates the basis and Cartier images exactly for \(n=3,5,7,9,11,13,15\). It checks the modular-index transition for every basis element, the unique omitted antipodal pair, the vanishing of \(\mathcal C^n\), and the two explicit maximal chains. It returns `VERIFY_OK`. These finite computations check examples only; the modular and symbolic proof above establishes the statement for every admissible odd \(n\).

## Relationship to prior work
Abdón, Bezerra and Quoos introduced the maximal curve family and established its genus and maximality. Garcia and Tafazolian proved the general upper nilpotency bound \(\mathcal C^n=0\) for curves maximal over \(\mathbb F_{2^{2n}}\). Shafighi's 2026 preprint obtains a monomial differential basis, a first-iterate Cartier formula and the \(a\)-number \(g/3\) for this specialization, but does not state the sharpness \(\mathcal C^{n-1}\ne0\), the two longest explicit chains, or the antipodal-index explanation. Almeida Filho, Tafazolian and Vieira analyze all Cartier ranks in a different family \(y^p-y=xR(x)\) for *odd* characteristic, and do not cover this characteristic-two four-sheeted family.

## Limitations
The theorem concerns only \(q=2\) within the larger Serre-type family \(X(q,n)\). It does not calculate every intermediate Cartier rank, the exact dimension of \(\operatorname{Im}(\mathcal C^{n-1})\) beyond the proved lower bounds, or the full Ekedahl–Oort type. The complete original 2009 construction paper was not accessible during this literature comparison; an equivalent earlier calculation outside inspected accessible sources remains a residual originality risk.

## References
1. Mahyar Shafighi, *The a-number of the Serre-type maximal curves of Abdón–Bezerra–Quoos*, arXiv:2610.15266v1 (11 October 2026), Sections 3, 4, 6.
2. Arnaldo Garcia and Saeed Tafazolian, *Certain maximal curves and Cartier operators*, *Acta Arithmetica* 135 (2008), 199–218, Theorem 3.3, DOI: 10.4064/aa135-3-1.
3. Miriam Abdón, Juscelino Bezerra and Luciane Quoos, *Further examples of maximal curves*, *Journal of Pure and Applied Algebra* 213 (2009), 1192–1196, DOI: 10.1016/j.jpaa.2008.11.037.
4. Gilberto B. Almeida Filho, Saeed Tafazolian and Stéfani C. Vieira, *a-Numbers, higher Cartier ranks and maximality of van der Geer–van der Vlugt curves*, arXiv:2610.17476v1 (12 October 2026), Introduction and Theorems A–C.
