# A sharp one-expanding-visit obstruction for piecewise-linear doubling maps

## Finding
For the piecewise-linear perturbation of the doubling map introduced by Bhattacharyya and Banerjee, **a regular attracting cycle with exactly one visit to the expanding half-circle can have at most three visits to the contracting half-circle**. This bound is sharp: an explicit attracting four-cycle has itinerary \(+---\). In particular, for every integer \(n\ge5\), the primitive itinerary comprising one \(+\) followed by \(n-1\) occurrences of \(-\) is impossible for any parameter. This gives a negative answer, already at period five, to the unrestricted realization question posed in Question 8.1 of the motivating paper (for regular attracting cycles).

## Assumptions and scope
For \(a\in\mathbb R/\mathbb Z\) and \(0\le b\le1\), write \(F_{a,b}\) for the continuous degree-two lift on \([0,1]\),
\[
F_{a,b}(x)=\begin{cases}
2(1+b)x+a-b/2,&0\le x\le1/2,\\
2(1-b)x+a+3b/2,&1/2\le x\le1.
\end{cases}
\]
The circle map is \(f_{a,b}(x)=F_{a,b}(x)\pmod1\), extended by degree two. Define \(I_+=(0,1/2)\), \(I_-=(1/2,1)\), and call a periodic orbit **regular** when it avoids \(0\) and \(1/2\). Its itinerary records \(+\) or \(-\) according to the location of each point. Attracting means that the absolute multiplier of the least-period return is strictly less than one. The claim concerns orbits whose complete cyclic itinerary has exactly one \(+\), not all possible attracting itineraries.

Let \(t=2(1-b)\) and \(u=2(1+b)=4-t\). An attracting orbit with itinerary \(+\underbrace{--\cdots-}_{k\text{ times}}\) has multiplier \(ut^k\). Thus \(t<1\); if \(t=0\), the contracting branch is constant and cannot contain multiple distinct successive points. Hence it suffices to treat \(0<t<1\).

## Proof
**Lemma (necessary visit inequality).** If a regular periodic cycle of length \(k+1\ge3\), with \(0<t<1\), has exactly one point in \(I_+\) and the other \(k\) points in \(I_-\), then
\[
H_{k-1}:=1+t+\cdots+t^{k-2}<(5-t)t^{k-1}.\tag{1}
\]

*Proof.* Number the distinct points consecutively as \(x_0\in I_+\), \(x_1,\ldots,x_k\in I_-\), with \(f(x_i)=x_{i+1}\) cyclically. Because the image under the negative affine lift of all of \(I_-\) has length \(t/2<1/2\), and different translates of the target interval \(I_-\) are separated by a gap of length \(1/2\), every transition \(x_j\mapsto x_{j+1}\), \(1\le j<k\), uses the same integer reduction. Their differences therefore satisfy
\[
x_{j+2}-x_{j+1}=t(x_{j+1}-x_j),\qquad 1\le j\le k-2.
\]
As the orbit has least period \(k+1\), \(d:=|x_2-x_1|>0\), and the negative-branch points are strictly monotone. In either ordering,
\[
H_{k-1}d=|x_k-x_1|<1/2.\tag{2}
\]

Suppose first that \(x_1>x_2>\cdots>x_k\). Then the last negative-to-positive transition cannot wrap at an integer: it reduces the output by \(t^{k-1}d<1/2\) from a representative in \((1/2,1)\). Consequently \(x_0=x_k-t^{k-1}d\). With \(\alpha=1/2-x_0\), this gives \(0<\alpha<t^{k-1}d\) and \(x_1-1/2=H_kd-\alpha\), where \(H_k=H_{k-1}+t^{k-1}\). The lift's increment between \(x_0\) and \(x_1\) is
\[
u\alpha+t(H_kd-\alpha)=r-d
\]
for an integer \(r\ge1\), since the corresponding circle images are \(x_1\) and \(x_2=x_1-d\). Therefore
\[
1\le r<(1+tH_{k-1}+ut^{k-1})d.
\]
Using (2), \(2H_{k-1}<1+tH_{k-1}+ut^{k-1}\). Since \((1-t)H_{k-1}=1-t^{k-1}\), this is precisely (1).

Alternatively suppose \(x_1<x_2<\cdots<x_k\). The final transition must wrap once at one, so \(x_0=x_k+t^{k-1}d-1\). Set \(\varepsilon=1-x_k\), obtaining \(0<\varepsilon<t^{k-1}d\) and \(x_0=t^{k-1}d-\varepsilon\). The lift increment from \(x_0\) to \(x_k\) is strictly between zero and two, and its reduction is \(x_0-x_1\); hence it equals \(r+x_0-x_1\), with \(r\in\{1,2\}\). Computing the same increment directly gives
\[
2-ut^{k-1}d+(u-t)\varepsilon=r-1+H_kd,
\]
so
\[
1\le3-r<(H_{k-1}+(u+1)t^{k-1})d.
\]
With (2), this again yields \(H_{k-1}<(u+1)t^{k-1}=(5-t)t^{k-1}\). This proves the lemma. \(\square\)

**Exclusion of four or more contracting visits.** For \(k\ge5\), divide (1) by \(t^{k-1}\):
\[
\sum_{j=1}^{k-1}t^{-j}<5-t.
\]
But for \(0<t<1\), Bernoulli's inequality gives \(t^{-j}\ge1+j(1-t)\). The first four terms already sum to at least \(4+10(1-t)>5-t\), a contradiction.

For \(k=4\), attraction requires \((4-t)t^4<1\). The function \((4-t)t^4\) is strictly increasing on \((0,1)\), and its value at \(t=3/4\) is \(1053/1024>1\). Thus \(t<3/4\). However
\[
\frac{H_3}{t^3}=t^{-3}+t^{-2}+t^{-1}\ge\frac{148}{27}>5>5-t,
\]
contradicting (1). Hence \(k\le3\) for all regular attracting cycles of the stated form.

**Exact sharpness.** Take \(a=203/5000\) and \(b=17/25\). With common denominator \(9312200\), the successive orbit points are
\[
\frac{3571863}{9312200},\quad
\frac{9213387}{9312200},\quad
\frac{6460887}{9312200},\quad
\frac{4699287}{9312200}.
\]
Direct substitution in the two affine branches gives the four transitions exactly, with integer reductions \(0,1,1,1\). These four points are distinct and strictly inside the required halves, in itinerary order \(+---\). Their return multiplier is
\[
(84/25)(16/25)^3=344064/390625<1.
\]
Thus the four-cycle is attracting and regular; three contracting visits are attainable. \(\square\)

## Verification
Run `python verify_orbit.py` with the Python standard library. It uses exact rational arithmetic to re-evaluate the four transitions, least period, branch inequalities, integer reductions, and return multiplier. It also checks rational instances of the inequalities in the universal proof; these finite tests support but do not replace the proof. The complete argument, rather than the sampled tests, establishes the exclusion for every parameter and every \(k\ge4\).

## Relationship to prior work
Bhattacharyya and Banerjee (2025), *On the Piecewise Linear Perturbations of the Doubling Map*, arXiv:2510.11441v1, define this family in Section 2, prove all single-minus itineraries are realized in Theorem 2.4, and prove a conditional characterization of non-single-minus regions in Theorem 2.5. Their Question 8.1 asks whether every itinerary containing a plus is realized by an attracting cycle for lengths at least four; the \(+----\) case is primitive and falls within its explicit wording. Their Lemma 4.1 excludes all-minus itineraries but not one-plus itineraries. The present one-plus obstruction is not implied by these results. Earlier work on analytic double-standard maps uses a different family and does not establish the stated piecewise-affine inequality.

## Limitations
The bound applies only to regular cycles with exactly one visit to \(I_+\). It does not rule out long contracting runs in cycles containing two or more expanding visits, or nonattracting or boundary-contact cycles. No parameter-space classification of all remaining itineraries is claimed. Bibliographic priority under alternative terminology cannot be guaranteed without broader external review. Independent validation has not been performed.

## References
1. A. Bhattacharyya and K. Banerjee, *On the Piecewise Linear Perturbations of the Doubling Map*, arXiv:2510.11441v1, posted 13 October 2025; Sections 2, 4, 5 and 8. https://arxiv.org/abs/2510.11441
2. M. Misiurewicz and A. Rodrigues, *Double Standard Maps*, Communications in Mathematical Physics (2007), cited as background in Reference 1.
