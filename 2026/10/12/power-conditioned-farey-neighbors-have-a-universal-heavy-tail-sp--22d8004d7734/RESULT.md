# Power-conditioned Farey neighbors have a universal heavy-tail spacing law

## Finding

For fixed integers \(r,s\ge2\), let \(\mathcal F_N\) be the increasing Farey sequence of order \(N\) including the endpoints \(0/1\) and \(1/1\). Let \(M_{r,s}(N)\) be the number of adjacent ordered pairs \(a/b<c/d\) in \(\mathcal F_N\) for which \(b=u^r\) and \(d=v^s\) for positive integers \(u,v\). The powers are exact powers, not powers with primitive bases. Define

\[
C_{r,s}=1-\frac{\Gamma(1+1/r)\Gamma(1+1/s)}{\Gamma(1+1/r+1/s)}>0,
\qquad \lambda_{r,s}=\frac1r+\frac1s.
\]

Then

\[
M_{r,s}(N)=\frac{C_{r,s}}{\zeta(2)}N^{\lambda_{r,s}}
 +O_{r,s}\big(N^{1/\min(r,s)}\log(2N)\big).
\tag{1}
\]

Choose a qualifying adjacent pair uniformly, and let its normalized gap be \(G_N=N^2(c/d-a/b)\). As \(N\to\infty\), the random variable \(G_N\) converges in distribution to \(G=1/(X^rY^s)\), with \((X,Y)\) uniform in the planar region

\[
\mathcal D_{r,s}=\{(x,y)\in(0,1)^2:x^r+y^s>1\}.
\]

In particular the limiting distribution has support \([1,\infty)\), and for \(t\ge1\) its cumulative distribution function is the explicit area integral

\[
\Pr(G\le t)=\frac1{C_{r,s}}
\int_0^1\int_0^1
\mathbf1_{\{x^r+y^s>1,\ x^ry^s\ge1/t\}}\,dx\,dy.
\tag{2}
\]

Writing \(\alpha_{r,s}=1+1/\max(r,s)\), the limiting upper tail satisfies

\[
\Pr(G>t)\sim K_{r,s}t^{-\alpha_{r,s}},\quad
K_{r,s}=\begin{cases}
1/[C_{r,s}s(r+1)],&r>s,\\
1/[C_{r,s}r(s+1)],&s>r,\\
2/[C_{r,r}r(r+1)],&r=s.
\end{cases}
\tag{3}
\]

Thus, for any real \(q>0\), the limiting moment \(\mathbb E[G^q]\) is finite **if and only if** \(q<\alpha_{r,s}\). For square-left and cube-right denominators, \(C_{2,3}=0.1586907368047273\ldots\), the count has order \(N^{5/6}\), and the limiting tail is asymptotic to \(t^{-4/3}/(8C_{2,3})\). Its mean is finite, but its variance is infinite.

## Assumptions and scope

Here \(N\) ranges through positive integers tending to infinity; \(r,s\) are **fixed** integers at least two. No primality or squarefreeness condition is imposed on the bases \(u,v\). The left/right orientation is retained when the exponents differ. Statements (2) and (3) concern the **limiting probability law**; no uniform-in-\(t\) statement is asserted for growing \(t=t(N)\). We use the usual Euler gamma and zeta functions. Big-O constants may depend on the fixed exponents.

## Proof

**Step 1: exact Farey correspondence.** The classical Farey-neighbor criterion says that a positive ordered denominator pair \((b,d)\) occurs exactly once for adjacent members of \(\mathcal F_N\) precisely when \(b,d\le N\), \(\gcd(b,d)=1\), and \(b+d>N\). This is Lemma 1 of Cobeli–Iordache–Zaharescu (2003); it also follows directly by solving \(bc-ad=1\) and using the mediant criterion. For \(N\ge2\), the possible exceptional pair \((1,1)\) is excluded by the strict sum condition. Therefore

\[
M_{r,s}(N)=\#\{(u,v)\in\mathbb N^2:
 u^r,v^s\le N,\ u^r+v^s>N,\ \gcd(u,v)=1\}.
\tag{4}
\]

The gap is exactly \(1/(bd)=1/(u^rv^s)\).

**Step 2: primitive lattice-point estimate.** Set \(U=N^{1/r}\), \(V=N^{1/s}\), and \(D=\min(U,V)\). For any fixed planar region obtained from \(\mathcal D_{r,s}\) by imposing finitely many inequalities with piecewise monotone rectifiable boundaries (in particular, the additional product conditions in (2)), its scaling by \((U,V)\) has area \(UV\) times the unscaled area and boundary length \(O_{r,s,t}(U+V)\). On a grid of mesh \(d\), its number of points differs from the area divided by \(d^2\) by \(O_{r,s,t}((U+V)/d+1)\): only cells meeting its rectifiable boundary are uncertain. Apply \(\mathbf1_{\gcd(u,v)=1}=\sum_{d\mid u,v}\mu(d)\) and sum over \(d\le D\). Since

\[
\sum_{d\le D}\frac{\mu(d)}{d^2}
=\frac1{\zeta(2)}+O(D^{-1}),
\qquad \sum_{d\le D}d^{-1}=O(\log(2D)),
\]

we obtain, for each such region of normalized area \(A\),

\[
\#\{(u,v)\text{ primitive in the scaled region}\}
=\frac{AUV}{\zeta(2)}
 +O_{r,s,t}\left(\frac{UV}{D}+(U+V)\log(2D)+D\right).
\tag{5}
\]

As \(UV/D=\max(U,V)\), the error is \(O_{r,s,t}(N^{1/\min(r,s)}\log(2N))\). The estimate is an infinite theorem, not a statement inferred from computations.

**Step 3: evaluate the area.** Integrating vertical sections of \(\mathcal D_{r,s}\),

\[
\operatorname{Area}(\mathcal D_{r,s})
=\int_0^1\left[1-(1-x^r)^{1/s}\right]dx
=1-\frac1r B(1/r,1+1/s)=C_{r,s}.
\]

Use this area in (5) and (4) to obtain (1). The region is open and nonempty, hence \(C_{r,s}>0\).

**Step 4: limiting spacing law.** Applying (5) to \(\mathcal D_{r,s}\) intersected with \(\{x^ry^s\ge1/t\}\) yields convergence of the distribution function of \(G_N\) to (2) for each fixed \(t\ge1\). The boundary curves have planar measure zero, so there are no atoms from boundary points. The map \((x,y)\mapsto 1/(x^ry^s)\) is continuous in the interior; its image of \(\mathcal D_{r,s}\) has closure \([1,\infty)\). This proves the claimed weak convergence and support.

**Step 5: tail and moments.** For large \(t\), the subregion \(x^ry^s<1/t\) of \(\mathcal D_{r,s}\) is confined to disjoint neighborhoods of the corners \((0,1)\) and \((1,0)\). Near \((0,1)\), its vertical width is \(1-(1-x^r)^{1/s}=x^r/s+O(x^{2r})\), and \(x<t^{-1/r}(1+o(1))\). Scaling \(x=t^{-1/r}z\), dominated convergence gives area

\[
\frac1{s(r+1)}t^{-(1+1/r)}(1+o(1)).
\]

Near \((1,0)\), by the symmetric calculation, the contribution is

\[
\frac1{r(s+1)}t^{-(1+1/s)}(1+o(1)).
\]

For sufficiently large \(t\) there is no contribution away from these corners, since there \(x^ry^s\) is bounded below. Divide by \(C_{r,s}\) and retain the slower-decaying term(s): this gives (3). Finally, the tail-integral identity \(\mathbb E[G^q]=q\int_0^\infty t^{q-1}\Pr(G>t)dt\) for \(q>0\), together with the positive tail constant, establishes exactly the stated moment threshold.

## Verification

The embedded standalone Python verifier uses two independent finite enumerations: (i) direct coprime power-coordinate search with the strict sum inequality, and (ii) the standard Farey-neighbor recurrence with denominator filtering. Their ordered denominator-pair sets agree for all \(45\) tested triples of parameters \((N,r,s)\), with \(N\in\{10,20,55,120,300\}\) and \(r,s\in\{2,3,4\}\). At \(N=10^7\), the direct counts for exponent pairs \((2,2),(2,3),(3,2),(3,3)\) are respectively \(1303766,66126,66126,3336\); the respective leading-term predictions are approximately \(1304622.73,65725.88,65725.88,3292.43\). The verification is finite corroboration; the proof is Steps 1–5 above.

To reproduce: run `python3 verify.py` using a standard Python 3 installation. No external packages or unstated input files are required.

## Relationship to prior work

The Farey-neighbor denominator criterion and the visible-lattice-point method are classical, particularly in Cobeli–Iordache–Zaharescu (2003), whose main theorem concerns relative denominator sizes after filtering the Farey sequence to odd denominators. Augustin–Boca–Cobeli–Zaharescu (2001) study spacings in the unfiltered Farey sequence; Cobeli–Vâjâitu–Zaharescu (2010) study gaps spanning an intermediate Farey point. Such results concern either positive-density denominator constraints or unconditioned gaps; they do not by themselves give the conditional law on the zero-density event that the two *adjacent full-Farey* denominators are perfect powers of independently fixed exponents. The new content here is the two-exponent thin-family count and especially its explicit limiting spacing distribution, corner tail, and sharp moment threshold. The derivation uses known elementary lattice-point machinery; no novelty is claimed for that machinery or for the neighbor criterion.

## Limitations

The asymptotic is for fixed exponents, not uniform when the exponents grow with \(N\). The limiting tail does not assert a uniform estimate for gaps at thresholds tending to infinity with \(N\). This is not the spacing law of the *filtered subsequence* of fractions whose denominators are powers: the fractions counted here remain adjacent in the original full Farey sequence. A possibly unindexed earlier treatment of this exact power-conditioned problem has not been excluded by an independent literature audit.

## References

1. V. Augustin, F. P. Boca, C. Cobeli, A. Zaharescu, “The h-spacing distribution between Farey points,” *Mathematical Proceedings of the Cambridge Philosophical Society* 131 (2001), 23–38, DOI: `10.1017/S0305004101005187` (publisher gives online publication date 2001-10-26).
2. C. Cobeli, A. Iordache, A. Zaharescu, “The relative size of consecutive odd denominators in Farey series,” *INTEGERS* 3 (2003), #A07, first published 2003-06-11, `https://emis.dsd.sztaki.hu/journals/INTEGERS/papers/d7/d7.pdf`.
3. C. Cobeli, M. Vâjâitu, A. Zaharescu, “On the intervals of a third between Farey fractions,” *Bulletin Mathématique de la Société des Sciences Mathématiques de Roumanie* 53 (2010), 239–250, `https://rms.unibuc.ro/bulletin/pdf/53-3/vajaitu1.pdf`.
4. OEIS A006843, denominators of Farey sequences; OEIS A308483, reciprocals of neighboring Farey gaps. These tabulate the unrestricted sequences and are used only for comparison.
