# The \((g-1)\)-secant locus lies in the Brill--Noether hypersurface
## Finding
Let \(X\) be a smooth projective curve of genus \(g\ge2\) over \(\mathbf C\), and let \(L\) be a line bundle of degree \(2g-1\). Write
\[
\mathbf P_L=\mathbf P\!\left(\operatorname{Ext}^1(L,\mathcal O_X)^*\right)
\]
for the extension space used by Biswas--Iyer, and let \(\mathcal H\subset\mathbf P_L\) be their degree-\(g\) determinantal hypersurface, whose points are precisely the extensions
\[
0\longrightarrow\mathcal O_X\longrightarrow E_e\longrightarrow L\longrightarrow0
\]
with \(h^0(X,E_e)\ge2\).

Then
\[
\operatorname{Sec}^{g-1}(X)\subset\mathcal H.
\]
More precisely, if \(D\) is any effective divisor of degree \(g-1\), then its span \(\overline D\subset\mathbf P_L\) is a linear \(\mathbf P^{g-2}\) and \(\overline D\subset\mathcal H\). In genus \(5\), every such degree-four divisor therefore supplies a \(\mathbf P^3\subset\mathcal H\subset\mathbf P^{12}\). This answers the linear-space existence question left open in Biswas--Iyer, Remark 3.8.

## Assumptions and scope
The statement is over \(\mathbf C\), with \(X\) smooth projective of genus \(g\ge2\) and \(\deg L=2g-1\). No genericity assumption on \(X\) or \(L\) is needed for the containment. The secant span \(\overline D\) is the one in the embedding \(X\hookrightarrow\mathbf P_L\) induced by \(K_X\otimes L\), as in the source paper.

## Proof
Fix an effective divisor \(D\) of degree \(g-1\). Biswas--Iyer recall the standard description
\[
\overline D=\mathbf P\!\left(\ker\bigl(H^1(X,L^{-1})\to H^1(X,L^{-1}(D))\bigr)^*\right).
\]
Thus, if \(e\in\overline D\), then the extension class \(e\in H^1(X,L^{-1})\) becomes zero after applying the map induced by the inclusion \(L(-D)\hookrightarrow L\). Equivalently, pulling the extension back along \(L(-D)\hookrightarrow L\) gives a split extension. Hence there is a lift
\[
\begin{array}{ccc}
& E_e & \\
& \uparrow & \searrow\\
L(-D)&\hookrightarrow&L,
\end{array}
\]
that is, a morphism \(L(-D)\to E_e\) whose composite with \(E_e\to L\) is the natural inclusion \(L(-D)\hookrightarrow L\).

Now \(\deg L(-D)=g\). Riemann--Roch gives
\[
h^0(X,L(-D))-h^0\!\left(X,K_X\otimes L^{-1}(D)\right)=g+1-g=1,
\]
so \(h^0(X,L(-D))\ge1\). Choose a nonzero section of \(L(-D)\) and lift it to a section of \(E_e\). Its image in \(L\) is nonzero, whereas the canonical section coming from \(\mathcal O_X\hookrightarrow E_e\) maps to zero in \(L\). These two sections are therefore linearly independent. Thus \(h^0(X,E_e)\ge2\), so \(e\in\mathcal H\). Since \(e\) was arbitrary, \(\overline D\subset\mathcal H\).

It remains only to record the dimension of the span. Because \(\deg L^{-1}(D)=-g<0\), one has \(h^0(X,L^{-1}(D))=0\). Riemann--Roch gives
\[
h^1(X,L^{-1})=3g-2,\qquad h^1(X,L^{-1}(D))=2g-1.
\]
The cohomology map is surjective, so its kernel has dimension \(g-1\). Hence \(\overline D\cong\mathbf P^{g-2}\). Taking the union over all effective \(D\) of degree \(g-1\) proves \(\operatorname{Sec}^{g-1}(X)\subset\mathcal H\).

For \(g=5\), the span has dimension \(3\), while \(\dim\mathbf P_L=3g-3=12\). Therefore \(\mathcal H\subset\mathbf P^{12}\) contains a \(\mathbf P^3\).

## Verification
The proof has two independent ingredients. First, functoriality of \(\operatorname{Ext}^1\) turns membership in the secant span kernel into a split pullback extension and hence a lift \(L(-D)\to E_e\). Second, Riemann--Roch forces a nonzero section of \(L(-D)\) because its degree is exactly \(g\). The lifted section is visibly independent of the canonical \(\mathcal O_X\)-section because their images in \(L\) differ. The numerical cohomology dimensions and genus-five specialization are replayed by `artifacts/verify_dimensions.py`.

## Relationship to prior work
Biswas--Iyer define the hypersurface \(\mathcal H\) by the condition \(h^0(E_e)\ge2\), recall Bertram's identification of the indeterminacy locus with \(\operatorname{Sec}^{g-1}(X)\), and in Remark 3.8 state that for \(g=5\) they do not know whether a \(\mathbf P^3\subset\mathcal H\subset\mathbf P^{12}\) exists. The argument above supplies the missing bridge: every degree-\((g-1)\) secant span already lies in \(\mathcal H\). Targeted searches of published-finding corpus and the public literature located no statement of this containment or of the resulting genus-five correction.

The result should not be confused with the standard fact that \(\operatorname{Sec}^{g-1}(X)\) is the unstable/indeterminacy locus of the extension map. The additional conclusion here is that this entire locus is contained in the determinantal Brill--Noether hypersurface.

## Limitations
The result proves the secant containment and the existence of the required linear spaces. It does not by itself assert unirationality of the particular genus-five hypersurface: the hypotheses of older quintic-unirationality results were not re-proved here from their primary full texts, and later literature describes some such results with additional generality assumptions. No claim about rationality, stable rationality, or the geometry of \(\mathcal H\) away from the secant locus is made.

## References
1. P. Biswas and J. N. N. Iyer, *A note on the Brill-Noether loci of small codimension in moduli space of stable bundles*, arXiv:2505.15749v2; first public version 21 May 2025. See Section 3, Lemma 3.3, Proposition 3.7, and Remark 3.8.
2. A. Bertram, *Stable pairs and log flips*, arXiv:alg-geom/9707002, for the extension-space/secant framework recalled by Biswas--Iyer.
