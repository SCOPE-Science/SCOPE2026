# The moment triangle of Euclidean parallelograms

## Finding

Let \(P\) be any nondegenerate Euclidean parallelogram. Sample two independent points \(X,Y\) uniformly by area and let \(R=\|X-Y\|_2\). Write \(M_{2j}=\mathbb E[R^{2j}]\), \(m=M_2>0\), and
\[
x=\frac{M_4}{M_2^2},\qquad y=\frac{M_6}{M_2^3}.
\]
The feasible set of normalized moment pairs \((x,y)\), taken over **all** positive-area parallelograms, is precisely the closed triangle with vertices
\[
A=\left(\frac{12}{5},\frac{54}{7}\right),\quad B=\left(\frac{17}{10},\frac{261}{70}\right),\quad C=\left(\frac{27}{10},\frac{153}{14}\right)
\]
**with the entire side \([A,C]\) removed**. The included edge \([A,B)\) consists of nonsquare rectangles, the included edge \([B,C)\) of nonsquare rhombi, and \(B\) is the square. The removed side comprises degenerate limiting shapes and is not attained by a genuine parallelogram.

Furthermore, the triple \((M_2,M_4,M_6)\) determines \(P\) uniquely up to Euclidean congruence, with an explicit inverse. By contrast, the pair \((M_2,M_4)=(1,2)\) is realized by a continuum of pairwise noncongruent parallelograms. Thus three consecutive even distance moments are a **sharp finite-moment reconstruction threshold** in this sense. On compact positive-area families with side lengths bounded above/below and acute edge-line angle bounded away from zero, the inverse is uniformly Hölder with exponent \(1/2\); this exponent cannot be improved on families containing rectangles.

## Assumptions and scope

The random points are sampled independently with replacement from normalized two-dimensional Lebesgue area measure, not uniformly along the boundary and not by an invariant-line chord convention. The metric is ambient Euclidean distance. A parallelogram can be written
\[
P=z_0+\{su+tv:0\le s,t\le1\},
\]
where \(u,v\in\mathbb R^2\) are linearly independent. Put \(\alpha=\langle u,u\rangle>0\), \(\beta=\langle v,v\rangle>0\), and \(\gamma=\langle u,v\rangle\) with \(\gamma^2<\alpha\beta\). Its congruence class is specified by the unordered side-length pair \(\{\sqrt\alpha,\sqrt\beta\}\) and the acute unoriented edge-line angle \(\phi=\arccos(|\gamma|/\sqrt{\alpha\beta})\in(0,\pi/2]\). No genericity assumptions are made.

## Proof

The coordinate differences of two independent uniform points of the unit square are independent random variables \(\xi,\eta\) with the triangular density \(1-|t|\) on \([-1,1]\). Their odd moments vanish and for each integer \(j\ge0\),
\[
\mathbb E[\xi^{2j}]=\mathbb E[\eta^{2j}]=\frac{2}{(2j+1)(2j+2)}.
\]
Since the affine mapping from the unit square to \(P\) has constant nonzero Jacobian, the squared distance is
\[
R^2=\alpha\xi^2+\beta\eta^2+2\gamma\xi\eta.
\]
Expansion and independence, using moments up to order six, yield **exactly**
\[
\begin{aligned}
M_2&=\frac{\alpha+\beta}{6},\\
M_4&=\frac{\alpha^2+\beta^2}{15}+\frac{\alpha\beta}{18}+\frac{\gamma^2}{9},\\
M_6&=\frac{\alpha^3+\beta^3}{28}+\frac{\alpha\beta(\alpha+\beta)}{30}
+\frac{2\gamma^2(\alpha+\beta)}{15}.
\end{aligned}
\tag{1}
\]
Set \(S=\alpha+\beta=6m\) and introduce the scale-invariant Gram parameters
\[
p=\frac{\alpha\beta}{S^2},\qquad q=\frac{\gamma^2}{S^2}.
\]
The positive-definite Gram condition and the arithmetic-geometric mean inequality are equivalent to
\[
0<p\le\frac14,\qquad0\le q<p.\tag{2}
\]
Conversely every pair satisfying (2) comes from a genuine parallelogram: take
\[
\{\alpha,\beta\}=\left\{\frac S2(1+\sqrt{1-4p}),\frac S2(1-\sqrt{1-4p})\right\},
\quad |\gamma|=S\sqrt q.
\]
The condition \(q<p\) is exactly \(\gamma^2<\alpha\beta\), so the Gram matrix is realizable by two linearly independent vectors in the plane.

Dividing (1) by powers of \(m=S/6\) gives the **affine** moment-coordinate map
\[
\boxed{x=\frac{12}{5}-\frac{14}{5}p+4q},\qquad
\boxed{y=\frac{54}{7}-\frac{558}{35}p+\frac{144}{5}q}.\tag{3}
\]
Its determinant is \(-2952/175\ne0\). The exact inverse is
\[
\boxed{p=\frac{93}{41}-\frac{70}{41}x+\frac{175}{738}y},\qquad
\boxed{q=\frac{81}{82}-\frac{155}{164}x+\frac{245}{1476}y}.\tag{4}
\]
Consequently (4), \(S=6m\), and the preceding Gram reconstruction determine both side lengths and the angle
\[
\phi=\arccos\sqrt{q/p}
\]
for every genuine parallelogram, without exceptions at \(p=1/4\) or \(q=0\).

The parameter region (2) is exactly the closed triangle with vertices \((p,q)=(0,0),(1/4,0),(1/4,1/4)\) minus its side \(q=p\), including both endpoints of that deleted side. The nonsingular affine image (3) is therefore precisely the claimed triangle minus \([A,C]\). Its two other sides have \(q=0\) (rectangles) and \(p=1/4\) (rhombi), respectively, and their intersection is the square. The limiting vertices \(A,C\) are approached, respectively, by ever more elongated rectangles and ever flatter equal-sided rhombi, so every displayed boundary is sharp.

To prove that two moments do not suffice, fix \(m=1\), choose any \(p\in[1/7,1/4]\), and put
\[
q=\frac7{10}p-\frac1{10}.
\]
All these pairs satisfy (2), and (3) gives \(x=2\). Therefore every resulting parallelogram has \((M_2,M_4)=(1,2)\). They are pairwise noncongruent because their recovered Gram parameter \(p\) varies continuously and strictly; their sixth moments vary accordingly.

For stability, consider any compact family with side lengths in \([\delta,L]\) and \(\phi\in[\delta,\pi/2]\), with \(0<\delta<L\) and \(\delta<\pi/2\). Here \(m\) stays bounded away from zero and infinity, \(p\) stays away from zero, and \(q/p\le\cos^2\delta<1\). Equations (4) are uniformly Lipschitz in the normalized moments. Recovering the two sorted side lengths uses only a bounded positive square root and \(\sqrt{1-4p}\), and recovering \(\phi\) uses \(\sqrt{q/p}\) followed by \(\arccos\) away from its singular endpoint. The inequality \(|\sqrt a-\sqrt b|\le\sqrt{|a-b|}\) proves uniform exponent \(1/2\). For sharpness, fix unequal side lengths and deform a rectangle through angles \(\phi=\pi/2-t\): both \(M_4\) and \(M_6\) change by \(O(t^2)\), while the angle changes by \(t\); no exponent larger than \(1/2\) can work in a neighborhood containing that rectangle.

## Verification

Run `python3 verify.py` from this package. Its exact-rational polynomial-expansion checks independently compute \(M_2,M_4,M_6\) as finite sums against the triangular coordinate law and compare them to (1); it also checks the inverse (4), the three vertices, and an explicit 101-shape continuum with the same first two moments. The program yielded `VERIFY_OK 7449 exact checks`, followed by a deterministic 200,000-sample comparison whose relative errors for orders two, four, and six were approximately \(0.00136\), \(0.00335\), and \(0.00572\). The universal theorem follows from the analytic proof above, not the finite tests.

## Relationship to prior work

The planar covariogram theorem of Averkov and Bianchi [1] concerns recovery from the **entire direction-labelled covariogram**. That much richer function determines a planar convex body and consequently any distance moments, but its injectivity does not imply that the three scalar moments here determine the shape. Gasparyan and Ohanyan [2] explicitly compute the covariogram and several random-line chord distributions of a parallelogram. Inspection of their formula sections finds no three-even-moment inverse theorem, no affine feasible-moment triangle, and no sharp two-moment ambiguity family. Their chord convention is not the independent uniform-endpoint convention used here. Martirosyan [3] handles direction-dependent chord statistics of arbitrary quadrilaterals, again retaining directional data and not proving this finite-statistic inverse theorem.

Two public geometric results supply important nearby comparisons: [4] calculates and sharply compares fourth moments between **boundary** and **interior** sampling on parallelograms, but does not involve sixth moments or invert the three interior moments; [5] reconstructs parallelograms using unlabeled **projection widths** rather than two-point distances. These claims neither contain nor imply the explicit affine map (3) with its complete feasible region. The proof above directly verifies the claim; search noncoverage is not treated as a general proof of historical priority.

## Limitations

The theorem concerns nondegenerate Euclidean parallelograms and exact population moments, not arbitrary convex quadrilaterals, finite-sample error bounds, or random-line chords. The stability constant deteriorates at degenerate sides or vanishing angle. The normalized moment triangle contains nonattainable degenerate boundary points, as explicitly stated. Earlier mathematical or engineering literature could contain an equivalent finite-moment reconstruction under another name; no independent scientific audit has been performed.

## References

[1] G. Averkov and G. Bianchi, *Confirmation of Matheron's conjecture on the covariogram of a planar convex body*, J. Eur. Math. Soc. 11 (2009), 1187–1202. First public preprint arXiv:0711.0572v1, 2007-11-05; journal version 2009. https://arxiv.org/abs/0711.0572; https://doi.org/10.4171/JEMS/179.

[2] A. G. Gasparyan and V. K. Ohanyan, *Covariogram of a Parallelogram*, Journal of Contemporary Mathematical Analysis 49 (2014), 194–206. https://doi.org/10.3103/S1068362314040050. Public full text available via the authors' ResearchGate entry.

[3] D. M. Martirosyan, *Orientation-Dependent Chord Length Distribution in a Convex Quadrilateral*, Journal of Contemporary Mathematical Analysis 58 (2023), 416–430. https://doi.org/10.3103/S1068362323060055.

[4] *Fourth-chord moment amplification and angular phase transition for parallelograms*, public mathematical research result (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-fourth-chord-moment-amplification-and-angular-phase-transition-f--45b0568cfb6e.

[5] *Three unlabeled width statistics reconstruct a parallelogram with sharp stability*, public mathematical research result (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-three-unlabeled-width-statistics-reconstruct-a-parallelogram-wit--dcfda0360928.
