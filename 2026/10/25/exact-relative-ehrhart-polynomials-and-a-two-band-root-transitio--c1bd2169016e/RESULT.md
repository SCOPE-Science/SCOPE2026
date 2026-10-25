# Exact relative Ehrhart polynomials and a two-band root transition for Reeve tetrahedra

## Finding
For every integer \(m\ge2\), let \(R_m\) be the lattice tetrahedron with vertices \((0,0,0)\), \((1,0,0)\), \((0,1,0)\), and \((1,1,m)\). Fix an integer \(L\ge1\) and the closed vertical segment \(Q_L=\{(0,0,z):0\le z\le L\}\). Write
\[
E_{m,L}(t)=\#\{a\in\mathbb Z^3:a+Q_L\subseteq tR_m\},\qquad q=\lfloor L/m\rfloor,\quad s=L-mq,\quad X=t-2q.
\]
For every integer \(t\ge0\), let \(\binom{v}{3}_{+}\) mean \(\binom v3\) when the integer \(v\ge3\), and zero otherwise. Then the **exact, not merely eventual** count is
\[
E_{m,L}(t)=\begin{cases}
\binom{X+3}{3}_{+}+(m-1)\binom{X+1}{3}_{+},&s=0,\\
(m-s+1)\binom{X+1}{3}_{+}+(s-1)\binom{X-1}{3}_{+},&1\le s<m.
\end{cases}
\]
The first \(t\ge0\) with \(E_{m,L}(t)>0\) is exactly \(t=2\lceil L/m\rceil\).

Replacing truncated binomial symbols by their polynomial counterparts gives the **eventual relative Ehrhart polynomial**
\[
F_{m,L}(t)=\begin{cases}
\dfrac{X+1}{6}\big[mX^2+(6-m)X+6\big],&s=0,\\
\dfrac{X-1}{6}\big[mX^2+(m+6-6s)X+6(s-1)\big],&1\le s<m.
\end{cases}
\]
Put \(r=1\) when \(s=0\), and \(r=s-1\) otherwise. Every \(F_{m,L}\) has three simple complex roots; precisely three of them are real when
\[
\Delta(m,r)=m^2-36mr+36r^2>0,
\]
and exactly one is real when \(\Delta(m,r)<0\). Equivalently, three real roots occur exactly for
\[
\frac rm<\frac{3-2\sqrt2}{6}\quad\text{or}\quad\frac rm>\frac{3+2\sqrt2}{6}.
\]
Equality is impossible for the stated integer parameters. The high-residue real-root regime \(1\le r\le m-2\) first becomes possible at \(m=70\), where \(r=68\) is admissible. In particular, the primitive segment \(L=1\) has \(F_{m,1}(t)=m(t-1)t(t+1)/6\) for every \(m\), although the usual Ehrhart polynomial of \(R_m\) has a nonreal pair for \(2\le m\le34\).

## Assumptions and scope
The parameters \(m\) and \(L\) are positive integers, with \(m\ge2\) and \(L\ge1\); \(t\) ranges over nonnegative integers for counting, and over the complex plane when locating roots of the eventual polynomial. All containment conditions are closed. The relative function counts integer translation vectors for the **fixed geometric segment** \(Q_L\); it does not scale the segment by \(t\). The segment need not be a subset of the original tetrahedron. This is not a statement about the ordinary Ehrhart polynomial or about weighted volumes of lattice segments.

## Proof
**Step 1: exact segment-containment inequalities.** The dilation \(tR_m\) is cut out by the four affine inequalities
\[
z\ge0,\quad mu-z\ge0,\quad mv-z\ge0,\quad m(t-u-v)+z\ge0.
\]
Consequently, a translated vertical segment with lower endpoint \((u,v,w)\in\mathbb Z^3\) lies inside \(tR_m\) if and only if
\[
w\ge0,\qquad mu\ge w+L,\qquad mv\ge w+L,\qquad m(u+v)\le mt+w.
\]
Sufficiency follows because each defining affine inequality is nonnegative at both endpoints and therefore throughout the segment.

**Step 2: sum the integer fibers exactly.** Write \(w=mj+e\), uniquely, with \(j\ge0\) and \(e\in\{0,\ldots,m-1\}\). Define \(c_e=\lceil(e+L)/m\rceil\). The inequalities become \(u,v\ge j+c_e\) and \(u+v\le t+j\), since \(\lfloor t+j+e/m\rfloor=t+j\). For a fixed fiber \((j,e)\), translating the first two coordinates shows that the number of integer pairs is
\[
\binom{t-j-2c_e+2}{2}_{+},
\]
where the analogous truncated quadratic binomial is zero unless the upper argument is at least two. The finite hockey-stick identity in \(j\) gives exactly
\[
E_{m,L}(t)=\sum_{e=0}^{m-1}\binom{t-2c_e+3}{3}_{+}.
\]
If \(s=0\), exactly one residue \(e=0\) has \(c_e=q\) and the remaining \(m-1\) residues have \(c_e=q+1\). If \(1\le s<m\), precisely \(m-s+1\) residues have \(c_e=q+1\) and the other \(s-1\) residues have \(c_e=q+2\). Substitution proves the displayed exact counts. The least positive summand appears at \(t=2q\) when \(s=0\) and at \(t=2q+2\) otherwise, giving the sharp nonemptiness threshold. For sufficiently large \(t\), every truncated binomial equals its polynomial formula; elementary factoring yields the two explicit cubics.

**Step 3: distinct roots and the phase diagram.** When \(s=0\), the linear factor is \(X+1\) and the quadratic factor is \(mX^2+(6-m)X+6\). Its discriminant is \(m^2-36m+36=\Delta(m,1)\); evaluating the quadratic at \(X=-1\) gives \(2m>0\), so no quadratic root coincides with the linear root. When \(1\le s<m\), put \(r=s-1\). The linear factor is \(X-1\), the quadratic is \(mX^2+(m-6r)X+6r\), and evaluating it at \(X=1\) gives \(2m>0\). Its discriminant is \(\Delta(m,r)\). If \(r=0\), this discriminant is \(m^2>0\). If \(r>0\), the equation \(\Delta=0\) would imply \(m/r=18\pm12\sqrt2\), impossible for positive integers. Hence all three roots are simple, and the sign of \(\Delta\) gives the real-root count. Dividing \(\Delta\) by \(m^2\) and solving its quadratic in \(r/m\) gives the two strict bands displayed above.

For the high-residue band among \(1\le r\le m-2\), the smallest possible discriminant in the relevant increasing branch becomes positive first at maximal residue \(r=m-2\). There \(\Delta=m^2-72m+144\), which is strictly positive for integers \(m\ge70\) and nonpositive for \(3\le m\le69\); when \(m=2\), the specified positive-residue range is empty. The endpoint \(m=70,r=68\) has \(\Delta=4\). For \(L=1\), \(s=1,r=0,q=0\), so the cubic factors exactly as stated. Finally, putting \(L=0\) in the counting derivation (outside the theorem's fixed positive-core scope) recovers the ordinary Reeve Ehrhart polynomial \(\frac m6t^3+t^2+(2-m/6)t+1\), whose discriminant \(m^2-36m+36\) is negative exactly for \(2\le m\le34\). This last comparison is classical, not a novel ordinary Ehrhart result.

## Verification
A standalone standard-library Python file `verify.py` enumerates all admissible integer translations independently from the four endpoint inequalities and compares them with the closed formula. It checks the polynomial factorization and quadratic discriminants by exact integer arithmetic, the sharp first nonempty dilation in sampled families, and both real-root sign regimes. The finite checks are supplementary: the three proof steps establish the claims for **every** permitted integer parameter.

## Relationship to prior work
Hirotsu's *Relative Ehrhart Functions: Eventual Polynomiality and Dualities*, arXiv:2608.10370 (first public 2026-08-11), establishes general eventual-polynomial behavior and duality phenomena for fixed-core relative Ehrhart counting. Its general polynomiality applies, but the special exact fiber formula and sharp cubic root classification are not given there. The paper's facet-touching extended-inscription assumptions for certain duality results do not apply to this vertical segment, which is not contained in \(R_m\).

Belyaev and Fayolle's *Counting Parallel Segments: New Variants of Pick's Area Theorem* (2019) considers the same Reeve tetrahedra and weighted whole/partial vertical lattice-segment valuations, including a calculation for Reeve height two. Those valuations are not the number of translates of an arbitrary *fixed* vertical segment contained in each dilation. Their displayed three-dimensional formulas do not state either present two-parameter relative Ehrhart law or the discriminant/root phase. Earlier classical work on Reeve tetrahedra describes the **ordinary** Ehrhart polynomial, corresponding to a point core, rather than the positive-length fixed segment considered here.

## Limitations
This classification concerns only lattice-aligned vertical segment cores and Reeve tetrahedra, not arbitrary segment directions or arbitrary lattice tetrahedra. The closed formula counts only nonnegative integer dilation parameters; the eventual cubic's complex roots are algebraic properties and are not counting values at negative \(t\). The root-sign phase is proven, but no assertion is made about analogous root laws for all relative Ehrhart functions. Historical-priority assessment remains provisional, especially older sources that might encode the fixed-segment count in alternative lattice-point language. No independent scientific audit is claimed.

## References
1. T. Hirotsu, *Relative Ehrhart Functions: Eventual Polynomiality and Dualities*, arXiv:2608.10370 (2026), https://arxiv.org/abs/2608.10370, first public 2026-08-11. Full text: https://arxiv.org/html/2608.10370v7.
2. A. Belyaev and P.-A. Fayolle, *Counting Parallel Segments: New Variants of Pick's Area Theorem*, *The Mathematical Intelligencer* **41** (2019), 1–7, https://doi.org/10.1007/s00283-019-09921-8. Open-access full text: https://d-nb.info/1206177764/34.
3. J. E. Reeve, *On the volume of lattice polyhedra*, Proc. London Math. Soc. (3) **7** (1957), 378–395. Ordinary Ehrhart formula used only for comparison.
