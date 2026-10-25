# A sharp logarithmic second correction for random tangent-triangle area tails

## Finding
Take three independent, uniformly distributed points of contact on the unit circle. Form their tangent lines and condition on the three supporting halfplanes having a bounded intersection containing the circle. Let \(S\) be the area of the resulting triangle. Then, as \(t\to\infty\),

\[
\boxed{\mathbb P\{S>t\}=\frac{12}{\pi t}+\frac{48\log t-12}{\pi^2t^2}+o(t^{-2}).}
\]

In particular, the second term is logarithmically enhanced, while the bounded-order coefficient at \(t^{-2}\) is exactly \(-12/\pi^2\). Equivalently, the triangle's perimeter \(P_T=2S\) satisfies
\[
\mathbb P\{P_T>p\}=\frac{24}{\pi p}+\frac{192\log(p/2)-48}{\pi^2p^2}+o(p^{-2}).
\]

The result concerns the full triangle area rather than the length of one randomly selected side.

## Assumptions and scope
The three contact angles are independent and uniform on \([0,2\pi)\), with the probability conditioned on all three cyclic gaps being strictly smaller than \(\pi\). This conditioning event has probability \(1/4\). Its complementary cases produce unbounded intersections of the three outward support halfplanes and are not included. Boundary events of zero measure are ignored. Area is Euclidean area, the circle has radius one, and \(t\) is an area threshold. No limit in the number of tangents is taken.

Write \(G_1,G_2,G_3\) for the consecutive contact-angle gaps, summing to \(2\pi\), and put
\[
a=(\pi-G_1)/2,\quad b=(\pi-G_2)/2,\quad c=(\pi-G_3)/2,\qquad L=\pi/2.
\]
Then \(a,b,c>0\) and \(a+b+c=L\). Their joint distribution is uniform on this triangle, with density \(2/L^2\) in \((a,b)\). Because consecutive tangent segments from each vertex have length \(\tan(G_i/2)\), the incircle-area identity gives the exact random variable
\[
S=\cot a+\cot b+\cot c.
\]

## Proof
**Step 1: exact boundary bands.** Define \(r=\operatorname{arccot}t\), and let \(E_t=\{S>t\}\). Because \(\cot a>t\) when \(a<r\), the union \(B_t=\{\min(a,b,c)<r\}\) lies in \(E_t\). For sufficiently large \(t\), \(r<L/3\). Direct inclusion-exclusion in the area-\(L^2/2\) simplex gives its unnormalized area
\[
|B_t|=3Lr-\frac92r^2=\frac{3L}{t}-\frac{9}{2t^2}+o(t^{-2}). \tag{1}
\]
Indeed, one strip has area \(Lr-r^2/2\), each pairwise overlap has area \(r^2\), and the triple overlap is empty.

**Step 2: partition the additional tail.** Set \(\eta=t^{-1/3}\). For all sufficiently large \(t\), the three corner squares, where two of \(a,b,c\) are at most \(\eta\), are pairwise disjoint. Outside these corners, an element of \(E_t\setminus B_t\) has exactly one coordinate \(a<3/t\), since if all coordinates were at least \(3/t\), then \(S\le 1/a+1/b+1/c\le t\). Thus, outside corners the excess lies in three disjoint middle edge strips with the other two coordinates at least \(\eta\).

Fix such a middle edge, and use \(a\) as its small coordinate and \(b\in[\eta,L-\eta]\) as the longitudinal coordinate. The threshold equation is
\[
\cot a+\cot b+\tan(a+b)=t.
\]
The relevant root \(a_*(b,t)>r\) is unique and lies between \(r\) and \(3/t\). Uniformly on the displayed interval, Taylor expansion and the derivative bound \(-\partial_a(\cot a+\tan(a+b))=t^2(1+o(1))\) at the root yield
\[
a_*(b,t)-r=\frac{\cot b+\tan b}{t^2}+O(t^{-3}\eta^{-2}). \tag{2}
\]
The portions within \(O(1/t)\) of the two artificial ends of the middle strip make only \(o(t^{-2})\) contribution. Integrating (2), the excess area from all three middle strips is
\[
\frac{3}{t^2}\int_\eta^{L-\eta}(\cot b+\tan b)\,db+o(t^{-2})
=\frac{6\log(\cot\eta)}{t^2}+o(t^{-2}). \tag{3}
\]
The error is \(O(t^{-3}\eta^{-2})=O(t^{-7/3})\) after integration, in particular smaller than \(t^{-2}\).

**Step 3: exact corner boundary layer.** In each corner, say \(a,b\le\eta\) and \(c=L-a-b\), restrict to \(a,b\ge r\), since the other points are already in \(B_t\). There
\[
S=\frac1a+\frac1b+O(\eta)
\]
uniformly. Replacing \(S>t\) by \(1/a+1/b>t\), and replacing the lower cutoff \(r\) by \(1/t\), changes this corner's area by \(o(t^{-2})\): the first error shifts the threshold by \(O(\eta)\), whose associated boundary-layer area derivative is \(O(\log(t\eta)/t^3)\); the second moves the cutoff by \(O(t^{-3})\) across a square of side \(\eta\).

Under \(A=ta\), \(B=tb\), and \(T=t\eta\), the remaining corner domain is
\[
1\le A,B\le T,\qquad A^{-1}+B^{-1}>1.
\]
For \(T>2\), its exact area is
\[
\begin{aligned}
J_T&=(T-1)\left(\frac{T}{T-1}-1\right)
+\int_{T/(T-1)}^T\frac{dA}{A-1}\\
&=1+2\log(T-1).
\end{aligned}
\]
All three corners therefore add
\[
\frac3{t^2}\left[1+2\log(t\eta-1)\right]+o(t^{-2}). \tag{4}
\]

**Step 4: cancellation of the cutoff.** Adding (1), (3), and (4) gives the unnormalized simplex area
\[
|E_t|=\frac{3L}{t}+\frac{6\log t-3/2}{t^2}+o(t^{-2}),
\]
since \(\eta\cot\eta\to1\) and \((t\eta-1)/(t\eta)\to1\). Multiplication by \(2/L^2\) and \(L=\pi/2\) proves the boxed theorem. The perimeter identity follows by substitution \(t=p/2\).

## Verification
A separate checker `verify.py` independently reconstructs the polygon from the three tangent-line equations, evaluates the area using the shoelace formula, simulates the conditional uniform angular-simplex model, and tests the asymptotic coefficients against a nonasymptotic one-dimensional quadrature. To derive the quadrature, fix \(b\) and note that the minimum over \(a+c=L-b\) is
\[
m(b)=\cot b+2\cot((L-b)/2).
\]
For \(t>3\sqrt3\), let \(b_-<L/3<b_+\) solve \(m(b)=t\). At intermediate \(b\), the length of the eligible \(a\)-interval is
\[
L-b-\arccos\left(\sin b+\frac{2\cos b}{t-\cot b}\right).
\]
Outside that interval, every \(a\) is eligible. Integrating the interval lengths and multiplying by \(2/L^2\) yields an exact one-dimensional integral for each tail probability. This is an independent finite-threshold check of the asymptotic proof. The numerical checker reports convergence of the renormalized constant to \(-12/\pi^2\), but no finite computation establishes an asymptotic statement.

## Relationship to prior work
Finch (2011), *Three Random Tangents to a Circle*, studies exactly this conditional tangent-line model, determines the density of a single side, and notes that the full perimeter density remains analytically intractable. The present theorem does not give a closed-form perimeter density; it instead determines the leading tail, the logarithmically enhanced second term, and the bounded second-order constant for the full area/perimeter. A side-length marginal does not determine these coefficients for the sum without its dependence structure. Xu (2015) studies random circumscribing polygons and limit theorems as the number of tangents grows; the accessible abstract does not establish a fixed-three-tangent tail expansion, but the full paper was unavailable for comparison. Related published research on randomly rotated tangential polygons concerns a distinct rotation model, not these three independent random normals.

## Limitations
This is a three-tangent, unit-circle result under conditioning on enclosure. It does not provide a closed-form density at all finite perimeter values, or analogous coefficients for four or more tangents or noncircular support curves. Historical priority, particularly against Xu's full 2015 paper and older random-triangle literature not accessed in full, remains subject to further checking. Independent mathematical validation has not been performed.

## References
- S. R. Finch, *Three Random Tangents to a Circle*, arXiv:1101.3931v1, first publicly posted 20 January 2011. https://arxiv.org/pdf/1101.3931
- W.-Q. Xu, *Random circumscribing polygons and approximations of π*, Statistics & Probability Letters 106 (2015), 52–57, DOI:10.1016/j.spl.2015.06.026. The accessible abstract was checked; full text could not be inspected.
- S. Wang, W.-Q. Xu and J. Liu, *Random Polygons and Optimal Extrapolation Estimates of pi*, Statistics, Optimization & Information Computing (2021), DOI:10.19139/soic-2310-5070-1193; concerned with large-sample random polygon approximation rather than a fixed-three-tangent upper tail.
