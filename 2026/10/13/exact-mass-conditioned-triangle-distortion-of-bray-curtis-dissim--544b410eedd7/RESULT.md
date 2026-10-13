# Exact mass-conditioned triangle distortion of Bray–Curtis dissimilarity

## Finding

Fix three positive community-abundance totals \(a,b,c\). For vectors of nonnegative species abundances with those totals, the exact largest multiplicative failure of the Bray–Curtis triangle inequality depends only on the totals. It is attained with two species, regardless of how many additional species are available. The total abundance of the intermediate community alone determines whether a triangle-inequality failure is *possible*.

Set \(m=\min\{a,c\}\) and \(M=\max\{a,c\}\). The sharp distortion is

\[
R(m,b,M)=
\begin{cases}
\dfrac{m+b}{2m},&0<b\le m,\\[5pt]
\left(\dfrac{b-m}{m+b}+\dfrac{M+2m-b}{M+b}\right)^{-1},&m\le b\le m+M,\\[5pt]
\left(\dfrac{b-m}{m+b}+\dfrac{b-M}{M+b}\right)^{-1},&b\ge m+M.
\end{cases}
\]

For a fixed ordered triple of positive total abundances, some profiles violate the ordinary triangle inequality if and only if

\[
\boxed{\max\{m,M-2m\}<b<\frac{m+M+\sqrt{(m+M)^2+12mM}}{2}.}
\]

At both endpoints, the ordinary triangle inequality is valid for every such profile. In particular, all equal-total profiles obey it. The known unrestricted sharp universal multiplicative bound is \(3/2\); **that universal bound is not claimed as new**. The result here is the exact prescribed-total profile and associated mass-only threshold.

## Assumptions and scope

Let \(s\ge 2\) be an integer and let \(x,y,z\in\mathbb R_{\ge0}^{s}\setminus\{0\}\) denote communities on the same set of \(s\) labeled species. Zero abundance is permitted. Their strictly positive \(\ell^1\) totals are prescribed as \(\|x\|_1=a\), \(\|y\|_1=b\), and \(\|z\|_1=c\). For nonzero nonnegative vectors define

\[
B(u,v)=\frac{\|u-v\|_1}{\|u\|_1+\|v\|_1}.
\]

Consider the ratio \(B(x,z)/(B(x,y)+B(y,z))\), only when the denominator is nonzero. The maximum exists and is calculated exactly below. Allowing real nonnegative abundances is essential to the exact all-total realization statement; integer counts require integral prescribed totals and can use the displayed integer witnesses whenever totals are integral.

## Proof

Interchanging the endpoint communities preserves the ratio. Assume henceforth \(a=m\le c=M\). Put

\[
\alpha=\frac1{m+b},\qquad \beta=\frac1{M+b},\qquad
u_0=|m-b|,\qquad v_0=|M-b|.
\]

Then \(\alpha\ge\beta>0\). Let \(u=\|x-y\|_1\), \(v=\|y-z\|_1\), \(w=\|x-z\|_1\). The reverse triangle inequality and ordinary \(\ell^1\) triangle inequality give

\[
u\ge u_0,\qquad v\ge v_0,\qquad u+v\ge w,\qquad 0\le w\le m+M.
\]

From these constraints, using \(\alpha\ge\beta\),

\[
\begin{aligned}
\alpha u+\beta v
&=\beta(u+v)+(\alpha-\beta)u\\
&\ge\beta\max\{w,u_0+v_0\}+(\alpha-\beta)u_0\\
&=\alpha u_0+\beta\max\{v_0,w-u_0\}=:g(w).
\end{aligned}
\]

The function \(g(w)\) is constant and nonnegative until \(w=u_0+v_0\), and thereafter is affine with slope \(\beta>0\) and nonnegative intercept \((\alpha-\beta)u_0\). Consequently \(w/g(w)\) is nondecreasing wherever defined for positive \(w\). If \(u_0=v_0=0\), the same conclusion holds because \(g(w)=\beta w\) for \(w>0\). Therefore, for positive denominator,

\[
\frac{B(x,z)}{B(x,y)+B(y,z)}
=\frac{w}{(m+M)(\alpha u+\beta v)}
\le \frac{m+M}{(m+M)g(m+M)}
=\frac1{g(m+M)}.
\]

To attain this bound, use two coordinates (and set all other coordinates to zero):

\[
x=(m,0),\qquad z=(0,M),\qquad
y=(\min\{m,b\},(b-m)_+),
\]

where \((t)_+=\max\{t,0\}\). Direct computation yields \(w=m+M\), \(u=u_0\), and \(v=\max\{v_0,m+M-u_0\}\). Thus equality holds in all the preceding inequalities. Evaluating \(g(m+M)\) for \(b\le m\), \(m\le b\le m+M\), and \(b\ge m+M\), respectively, gives all three asserted formulas. They agree on their shared boundaries.

For \(b\le m\), \(R\le1\). On \(m\le b\le m+M\), the denominator of the middle expression minus one is

\[
\frac{(m-b)(2m+b-M)}{(m+b)(M+b)}.
\]

Hence \(R>1\) precisely when both \(b>m\) and \(b>M-2m\). On \(b\ge m+M\), the last denominator minus one equals

\[
\frac{b^2-(m+M)b-3mM}{(m+b)(M+b)}.
\]

Thus \(R>1\) there exactly when \(b\) is below the displayed positive quadratic root. Combining these intervals gives the stated strict mass-only criterion. Equality at a boundary follows from \(R=1\).

## Verification

The accompanying `verify.py` enumerates every two-species nonnegative integral profile at all ordered mass triples with \(1\le m\le M\le8\) and \(1\le b\le8\), and every three-species profile at \(1\le m\le M\le4\), \(1\le b\le4\), using exact rational arithmetic. It additionally verifies an attaining two-species profile for each tested mass triple. The computation is finite; the proof above, rather than enumeration, establishes the theorem for arbitrarily large species sets and all positive real totals.

## Relationship to prior work

Bray and Curtis (1957) introduced the motivating ecological dissimilarity framework. Gragera and Suppakitpaisarn (2016; expanded 2018) established the **unrestricted** sharp \(3/2\) relaxed triangle-inequality factor for the set-based Sørensen–Dice index. That factor, the nonmetricity of Bray–Curtis, and the equal-total reduction to normalized \(\ell^1\) distance are background, not novel claims here. Ricotta and Podani (2017) analyzed additional ecological properties of Bray–Curtis; Greenacre (2017) explains why overall community size and relative species composition must be distinguished. The new mathematical statement is the sharp **conditional** ratio for every fixed ordered triple of total abundances, including exact critical boundaries and universally attaining two-species profiles. Full text of the most relevant Gragera–Suppakitpaisarn work was not obtainable, so an unrecognized stronger conditional result there remains an originality risk.

## Limitations

This is a deterministic mathematical theorem, not an empirical estimate. It does not estimate sampling variation, require integer census counts, or guarantee violations for a particular observed triple merely because their totals lie inside the permissive interval. It characterizes existence over *all* nonnegative species profiles with specified totals. Outside the interval no profile with those totals can violate the triangle inequality. One-species communities are excluded from the two-species attainment statement. A plausible earlier source may contain a broader conditional formula than was accessible for inspection; originality is consequently qualified, not independently certified.

## References

- J. R. Bray and J. T. Curtis (1957), “An Ordination of the Upland Forest Communities of Southern Wisconsin,” *Ecological Monographs* 27, 325–349. DOI: 10.2307/1942268.
- A. Gragera and V. Suppakitpaisarn (2016), “Semimetric Properties of Sørensen-Dice and Tversky Indexes,” *WALCOM 2016*, 339–350. DOI: 10.1007/978-3-319-30139-6_27.
- A. Gragera and V. Suppakitpaisarn (2018), “Relaxed triangle inequality ratio of the Sørensen–Dice and Tversky indexes,” *Theoretical Computer Science* 718, 37–45. DOI: 10.1016/j.tcs.2017.01.004.
- C. Ricotta and J. Podani (2017), “On some properties of the Bray–Curtis dissimilarity and their ecological meaning,” *Ecological Complexity*. DOI: 10.1016/j.ecocom.2017.07.003.
- M. Greenacre (2017), “‘Size’ and ‘shape’ in the measurement of multivariate proximity,” *Methods in Ecology and Evolution*. DOI: 10.1111/2041-210x.12776.
