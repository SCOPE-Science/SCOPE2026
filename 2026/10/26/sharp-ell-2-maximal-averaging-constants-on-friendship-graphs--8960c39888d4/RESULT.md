# Sharp \(\ell^2\) maximal-averaging constants on friendship graphs

## Finding
For each integer \(m\ge2\), put \(F_m=K_1\vee(mK_2)\), so the graph has one hub and \(m\) disjoint pairs of adjacent outer vertices, each joined to the hub. On this graph with counting measure, define the centered graph-ball maximal operator
\[M_m f(v)=\max_{r=0,1,2}\frac1{|B(v,r)|}\sum_{w\in B(v,r)}|f(w)|.\]
(The radius-one hub ball and all radius-two balls are the whole graph.) Then the exact sharp strong \(\ell^2\) norm is
\[\boxed{\|M_m\|_{\ell^2\to\ell^2}^2=\lambda_m=\frac{2m+13+\sqrt{(2m+13)^2-144}}{18}.}\]
It is attained by positive inputs with hub value \(h\), uniform outer value \(a>0\), and
\[\frac ha=\frac{9\lambda_m-4}{2}.\]
Consequently \(\|M_m\|_{2\to2}=\frac{\sqrt{2m}}3(1+\frac{13}{4m}+O(m^{-2}))\).
The special case \(m=1\) is the known three-vertex complete graph and is included only as a verification check, not as the new result.

## Assumptions and scope
The graph is finite, simple, unweighted, connected, and its balls use shortest-path distance and uniform counting averages. The stated norm is the optimal constant in \(\|M_m f\|_2\le\|M_m\|_{2\to2}\|f\|_2\), over all real or complex functions on vertices. Since \(M_m f=M_m|f|\), nonnegative inputs suffice. This is the **centered**, not the uncentered, maximal operator; no assertions are made for other exponents or arbitrary windmills.

## Proof
Write \(N=2m+1\). At a hub, the possible averaging rows are its coordinate row \(e_0\) and the uniform row \(u=(1/N,\ldots,1/N)\). At either outer vertex \(i\) of a pair \(\{i,i'\}\), the possible rows are \(e_i\), the local triangle average \(t_i=(e_0+e_i+e_{i'})/3\), and \(u\). For a fixed nonnegative input, each coordinate of \(M_m f\) is the maximum of these linear row values. Therefore
\[\|M_m\|_{2\to2}^2=\max_{A\in\mathcal A_m}\lambda_{\max}(AA^\mathsf T),\]
where \(\mathcal A_m\) consists of matrices formed by choosing independently one allowed row at each output vertex. This identity follows by interchanging two finite maxima and by Perron--Frobenius: a maximizing singular input for a nonnegative matrix can be chosen nonnegative.

Let \(B\) choose the hub identity row and all local triangle-average rows. Its nonzero top singular sector is the two-dimensional space of inputs constant on outer vertices. In orthonormal hub/outer coordinates the matrix is
\[\begin{pmatrix}1&0\\\sqrt{2m}/3&2/3\end{pmatrix}.\]
The larger eigenvalue of its Gram matrix is \(\lambda_m\), and its other singular sectors have squared norm at most \(4/9\). Let \(y=(r,1,\ldots,1)\) be the strictly positive Perron vector of \(BB^\mathsf T\). Direct computation gives
\[r=\frac{2m}{3(\lambda_m-1)},\qquad 1<r<3,\qquad BB^\mathsf T y=\lambda_m y.\]
For \(m\ge2\), the inequality \(1<r<3\) follows from the displayed radical expression; it is also exact at \(m=1\), where \(r=2\).

For \(m\ge5\), fix any choice matrix \(A\). All rows are nonnegative and sum to one. In \(AA^\mathsf T y\), a local triangle-average row receives no greater contribution from any other row than does the corresponding row of \(BB^\mathsf T y\): the overlap with the hub identity is \(1/3\), with its paired leaf's identity or triangle row at most \(1/3\), and with rows on another triangle at most \(1/9\). The last comparison includes a global row because \(1/N\le1/9\) for \(m\ge4\). Thus its component is at most \(\lambda_m\). A global row gives exactly \((r+2m)/N<\lambda_m\). A leaf identity row has weighted overlap bounded strictly by
\[1+\frac13+\frac{2m-2+r}{N}<\frac73<\lambda_5\le\lambda_m.\]
For the hub identity row the component is at most \(r+2m/3=\lambda_m r\), and for a global hub row it is \((r+2m)/N\le r<\lambda_m r\). Hence \(AA^\mathsf T y\le\lambda_m y\) coordinatewise. The Perron--Frobenius comparison inequality gives \(\lambda_{\max}(AA^\mathsf T)\le\lambda_m\).

For \(m=4\), the same comparison applies when the hub row is its identity: a leaf identity row is bounded by \(4/3+6/9=2<\lambda_4\). When the hub row is global, instead use the all-one comparison vector. Global rows then give row sum one; local triangle rows have sum at most \(2/3+6/9+1/9=13/9\), and leaf identity rows at most \(4/3+7/9=19/9<\lambda_4\). The strict inequalities follow from \(\lambda_4=(21+\sqrt{297})/18>19/9\). This proves the bound for \(m=4\).

For \(m=2,3\), the finite exact certificate in `check_friendship.py` checks all independent radius selectors up to permutation of entire triangles (respectively \(90\) and \(330\) cases; it also checks \(18\) cases for the known \(m=1\) benchmark). It multiplies the averaging matrix by \(3N\), computes the exact integer characteristic polynomial of twice the resulting row Gram matrix using Faddeev--LeVerrier, and substitutes the exact algebraic threshold \(N^2(2m+13+\sqrt{(2m+13)^2-144})\). Every coefficient of the shifted real-rooted characteristic polynomial is nonnegative, verified by exact integer comparisons in the quadratic field. Because the polynomial is real-rooted, nonnegative coefficients preclude a positive root, proving all Gram eigenvalues are at most \(\lambda_m\). Thus the finite checks are exhaustive exact certificates, not floating-point experiments.

Finally the positive right singular vector of \(B\) has outer value \(a>0\) and hub ratio \(h/a=(9\lambda_m-4)/2>1\). At this input the hub chooses its singleton average, and each leaf chooses its triangle average: indeed \((h+2a)/3\ge a\) and for \(m\ge2\) exceeds the global mean \((h+2ma)/N\). Therefore \(M_m f=Bf\) and equality is attained. Expanding the exact radical gives the stated asymptotic.

## Verification
Run `python3 check_friendship.py` in the same directory; the program requires only the Python standard library. It verifies all \(18+90+330=438\) radius-selection equivalence classes exactly for \(m=1,2,3\), without numerical tolerances. Its nonnegative-coefficient test is logically equivalent to positive semidefiniteness of the comparison matrix because that matrix is symmetric. The case \(m\ge4\) is proved above analytically; it is not inferred from a finite search.

## Relationship to prior work
Soria and Tradacete (arXiv:1410.6204v1, 2014) introduced sharp finite-graph centered maximal inequalities, proving general results for \(0<p\le1\) and treating complete and star graphs. González-Riquelme and Madrid (arXiv:2005.03146, 2020) determined the sharp \(\ell^2\) norms for complete and star graphs. Their sequel (arXiv:2011.02630, 2020) developed extremizers and further estimates for those two families. These are distinct from the present family of \(m\) triangles sharing a hub; the known \(m=1\) complete-graph case is not claimed. The present claim is the exact all-\(m\) friendship-graph strong \(\ell^2\) norm and its attained extremizer.

## Limitations
Historical priority has not been established exhaustively: specialist work on cones over matching graphs or equivalent metric-ball averaging schemes may be unindexed. The finite coefficient certificate must be replayed from the included source to validate its computational premise; no independent audit is claimed. No statement about arbitrary weighted graphs, other exponents, or uniqueness of maximizing inputs is proved.

## References
- J. Soria and P. Tradacete, *Best constants for the Hardy--Littlewood maximal operator on finite graphs*, arXiv:1410.6204v1 (22 October 2014), https://arxiv.org/abs/1410.6204.
- C. González-Riquelme and J. Madrid, *Sharp Inequalities for maximal operators on finite graphs*, arXiv:2005.03146 (first posted 6 May 2020), https://arxiv.org/abs/2005.03146.
- C. González-Riquelme and J. Madrid, *Sharp inequalities for maximal operators on finite graphs, II*, arXiv:2011.02630 (5 November 2020), https://arxiv.org/abs/2011.02630.
