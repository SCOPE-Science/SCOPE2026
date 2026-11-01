# Exact exceptional-set dimension and first-entrance laws in eventually periodic chaotic interval maps

## Finding
For the Khan–Rajan piecewise-affine interval maps, the measure-zero set of points that never enter the periodic intervals has an **exact, nonzero Hausdorff dimension**. The same first-return geometry gives the **complete distribution of first entrance**, including an independent, parameter-independent entrance-phase law and a sharp exponential critical scaling.

Fix an integer \(p\ge3\) and a real number \(m>1\). Put
\[
B=\sum_{j=0}^{p-1}m^j,\qquad R=\sum_{j=0}^{p-2}m^j,\qquad
b_-=B^{-1},\quad b_+=R^{-1},
\]
and choose \(b_-<b<b_+\). Define \(L=bR\), \(h=(1-b)/m\), and \(\delta=L-h=(Bb-1)/m\). On \([0,1]\), let
\[
f(x)=\begin{cases}
mx+b,&0\le x\le h,\\
(L-x)/\delta,&h\le x\le L,\\
(x-L)/m^{p-1},&L\le x\le1.
\end{cases}
\]
Define the closed periodic intervals
\[
C_j=\left[b\sum_{i=0}^{j-1}m^i,\;m^{-(p-j-1)}\Big(1-b\sum_{i=0}^{p-j-2}m^i\Big)\right],\quad 0\le j<p,
\]
with empty sums interpreted as zero, and write \(C=\bigcup_{j=0}^{p-1}C_j\). Every point of \(C\) has period \(p\) under \(f\), as established in the motivating paper.

Let \(E=\{x\in[0,1]:f^n(x)\notin C\text{ for all }n\ge0\}\). Put
\[
A=\sum_{s=0}^{p-2}m^{-s},\qquad q=A\delta=\frac{b-b_-}{b_+-b_-},\qquad
c=1-q,\qquad v_s=\frac{m^{-s}}{A}.
\]
Then \(0<q,c<1\) and:

**(Geometry)** There is a unique \(d\in(0,1)\) such that
\[
\boxed{\dim_H E=d,\qquad \sum_{s=0}^{p-2}\left(\frac{\delta}{m^s}\right)^d=1.}
\]
In particular, the null exceptional set has positive dimension for every interior parameter, increases continuously from dimension zero to dimension one as \(b\) traverses its admissible interval, and obeys the sharp endpoint laws
\[
 d\sim\frac{\log(p-1)}{|\log q|}\quad(b\downarrow b_-),
\qquad
1-d\sim\frac{c}{H(v)}\quad(b\uparrow b_+),
\]
where \(H(v)=-\sum_{s=0}^{p-2}v_s\log v_s>0\).

**(First-entrance law)** For a Lebesgue-uniform starting point \(X\in[0,1]\), set \(T=\min\{n\ge0:f^n(X)\in C\}\). Then \(T<\infty\) almost surely and
\[
\boxed{\mathbb E[z^T]=\frac{c}{1-q\sum_{s=0}^{p-2}v_s z^{s+1}}}\qquad(|z|\le1).
\]
Equivalently, \(T\) has the law of the sum of \(N\) independent lengths \(D_i\), where \(\Pr(N=k)=cq^k\) for \(k\ge0\), and \(\Pr(D_i=s+1)=v_s\). If \(\mu=\sum_s(s+1)v_s\) and \(\sigma^2=\sum_s(s+1-\mu)^2v_s\), then
\[
\mathbb ET=\frac{q\mu}{c},\qquad
\operatorname{Var}T=\frac{q\sigma^2}{c}+\frac{q\mu^2}{c^2},\qquad
\boxed{\frac{cT}{\mu}\ \Longrightarrow\ \mathrm{Exp}(1)}\quad(b\uparrow b_+).
\]
In particular, \(\mathbb ET\sim \mu(b_+-b_-)/(b_+-b)\).

**(Entrance location)** With \(Y=f^T(X)\in C\), \(Y\) is uniform on \(C\) and independent of \(T\). If \(J\) is the index satisfying \(Y\in C_J\), then
\[
\boxed{\Pr(J=j\mid T=n)=\frac{m^j}{B}}\qquad(0\le j<p,\ n\ge0\text{ with }\Pr(T=n)>0).
\]
These statements concern Lebesgue-distributed starting states, not an arbitrary invariant initial probability.

## Assumptions and scope
The strict bounds \(b_-<b<b_+\), \(m>1\), and integer \(p\ge3\) are essential to the stated strong separation and positive measure of the periodic intervals. There are no random dynamical choices: randomness enters only through the initial uniform point. The limiting laws keep \(p,m\) fixed while \(b\) varies. The endpoints of the partition form a finite/countable exceptional collection and have no effect on Hausdorff dimension or Lebesgue first-entrance probabilities.

## Proof
**1. Exact Markov geometry.** The intervals \(C_0,\ldots,C_{p-1}\) are disjoint and cyclically mapped onto one another. Their intervening gaps \(U_s\), indexed so \(U_0=(h,L)\) and \(U_s\) lies between \(C_{p-2-s}\) and \(C_{p-1-s}\), satisfy \(f(U_s)=U_{s-1}\) for \(s\ge1\), while \(f(U_0)=(0,1)\). These facts follow by substituting the displayed affine formulas at every endpoint. Their lengths are
\[
|U_s|=\delta m^{-s}=qv_s,\qquad |C_j|=c\frac{m^j}{B}.
\]
In particular, the total gap length is \(q\) and the total periodic-interval length is \(c\). Direct substitution yields \(q=(b-b_-)/(b_+-b_-)\).

**2. First-return similarities and dimension.** Every orbit staying in the gaps visits \(U_0\) repeatedly, because each \(U_s\) deterministically reaches \(U_0\) in \(s\) iterates. A first return from \(U_0\) through \(U_s\) lasts \(s+1\) iterates. With \(S_s=\sum_{i=0}^{s-1}m^i\), the inverse first-return branch on \(U_0\) is the explicit affine similarity
\[
\phi_s(w)=L-\frac{\delta}{m^s}(w-bS_s),\qquad 0\le s\le p-2.
\]
Indeed, \(f(\phi_s(w))=(w-bS_s)/m^s\in U_s\), and the next \(s\) iterates equal \(w\). The images \(\phi_s(U_0)\) are pairwise disjoint, strictly contained in \(U_0\), and separated by positive gaps, since the complementary \(C_j\) have positive length. Their contraction ratios are \(r_s=\delta m^{-s}<1\). The closure of \(E\cap U_0\) is the compact attractor of this finite similarity system, up to countably many boundary itineraries. Strong separation and the elementary similarity-dimension theorem give the unique root \(\sum_s r_s^d=1\). The whole of \(E\) consists of finitely many affine preimages of \(E\cap U_0\), together with at most countably many partition-boundary exceptions; hence it has the same dimension.

Since \(\sum_s r_s=q<1\), the root lies below one; since there are \(p-1\ge2\) positive contractions, the root is positive. The defining sum increases strictly with \(b\), so \(d\) is continuous and strictly increasing. Writing \(r_s=qv_s\), the equation becomes \(q^d\sum_s v_s^d=1\). As \(q\downarrow0\), \(d\downarrow0\) and \(d\log q+\log\sum_s v_s^d=0\) gives the first endpoint equivalent. As \(q\uparrow1\), implicit differentiation at \((q,d)=(1,1)\), where the derivatives are \(1\) and \(-H(v)\), gives \(1-d\sim(1-q)/H(v)\).

**3. Exact Markov renewal and entrance.** Conditional on a Lebesgue-uniform point lying in a gap, its location is uniform there. All gap transitions are affine and onto the specified next gap, so this conditional uniformity is preserved after conditioning on any finite gap itinerary. From \(U_0\), the map is affine onto \((0,1)\), giving probability \(c\) of reaching \(C\), and probability \(qv_s\) of going to \(U_s\). Each chosen \(U_s\) reaches \(U_0\) after exactly \(s\) more iterates. The initial uniform state is already in \(C\) with probability \(c\), or in \(U_s\) with probability \(qv_s\). Thus the number of traversed gaps before absorption is geometric with success probability \(c\), and the total time is the claimed compound-geometric sum with i.i.d. lengths \(s+1\). Summation gives the generating function, mean and variance. Its Laplace transform at \(z=\exp(-sc/\mu)\) tends to \((1+s)^{-1}\) for every \(s\ge0\), establishing the exponential law.

Finally, each successful passage from \(U_0\) sends conditional uniform mass uniformly across \(C\) because the map is affine and onto \((0,1)\). The same is true at \(T=0\), by restriction of the initial Lebesgue law. Hence the entrance location is uniform on \(C\), independently of every finite history determining \(T\). Since \(|C_j|/|C|=m^j/B\), the phase law follows.

## Verification
The included standalone `CHECK.py` uses exact rational arithmetic to build the original branch partition, follow every feasible finite gap itinerary, and compare first-entrance masses and entrance phases with the generating function. It also verifies the explicit first-return similarities' endpoints and contraction ratios. The executed tests cover \((p,m,b)=(3,2,1/5),(4,3/2,1/7),(5,2,1/20)\) through respectively 9, 7, and 6 entrance steps, with exact mean/variance identities. Numerical bisection of the dimension equation supplies illustrative roots \(0.358299230919\), \(0.419942844123\), and \(0.647316499848\). These finite checks and numerical roots are not the proof of the dimension or asymptotic laws; those follow from the similarities and renewal arguments above.

## Relationship to prior work
Khan and Rajan (2017) defined exactly this piecewise-affine family, its cyclic periodic intervals and intervening gaps, and proved almost-everywhere eventual period \(p\), using a finite transition matrix. Those basic results and the matrix are credited here. That paper establishes disappearance of survivor **Lebesgue measure**, but does not state the survivor's Hausdorff dimension, its exact parameter dependence and endpoint exponents, the compound-geometric first-entrance law, or independence of the entrance phase. The present first-return similarity construction and weighted dimension equation provide genuinely finer geometry than the previously used unweighted measure matrix. Generic similarity-dimension and finite-state renewal principles are standard methods; their application to this explicit family, rather than the methods themselves, is the claim.

## Limitations
The exceptional set is defined using first **entry into the union of periodic intervals**, not the much larger set of states that happen to be periodic without entering it. No claim is made about the exact Hausdorff measure at the critical dimension, external noise, general non-affine perturbations, or nonuniform initial distributions. The critical limits do not include the degenerate endpoint parameter maps. Relevant older interval-repeller and symbolic-coding literature could contain an equivalent dimension formula under another description; targeted comparisons did not establish exhaustive publication priority. Independent validation has not been performed.

## References
1. M. Ali Khan and Ashvin V. Rajan, “On the eventual periodicity of piecewise linear chaotic maps,” *Bulletin of the Australian Mathematical Society* 95 (2017), 467–475. DOI: 10.1017/S0004972716001313. First published online 2017-02-16; full article inspected at https://www.cambridge.org/core/services/aop-cambridge-core/content/view/0D906FB79F6DCE0E60959B845D9B1235/S0004972716001313a.pdf/on_the_eventual_periodicity_of_piecewise_linear_chaotic_maps.pdf.
2. M. B. Nathanson, “Piecewise linear functions with almost all points eventually periodic,” *Proceedings of the American Mathematical Society* 60 (1976), 75–81. DOI: 10.1090/S0002-9939-1976-0417351-3. (Earlier construction; bibliographic record and available excerpt consulted.)
3. J. P. Gaivão, “Hausdorff Dimension of the Exceptional Set of Interval Piecewise Affine Contractions,” *Qualitative Theory of Dynamical Systems* 24 (2025), article 86. DOI: 10.1007/s12346-025-01246-6. (A different exception: a set of parameters of contracting maps, not noncaptured initial points in the Khan–Rajan maps.)
