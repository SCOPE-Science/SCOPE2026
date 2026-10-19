# Sharp one-sided logarithmic response of Parry measures at integer bases

## Finding

For an integer \(b\ge 2\), write \(T_\beta(x)=\beta x-\lfloor\beta x\rfloor\) on \([0,1)\), and let \(\mu_\beta\) be its canonical absolutely continuous invariant probability. Regard measures on the compact interval \([0,1]\). As \(\varepsilon=b-\beta\downarrow0\), with \(b-1<\beta<b\), the following **signed weak limit** holds:

\[
\frac{\mu_\beta-dx}{\varepsilon\log(1/\varepsilon)}\ \xrightarrow{\;\mathrm{weak}\;}\ \frac{dx-\delta_1}{b\log b}.
\]

Equivalently, for every fixed continuous \(\phi:[0,1]\to\mathbb R\),

\[
\int\phi\,d\mu_\beta-\int_0^1\phi(x)\,dx
=\frac{\varepsilon\log(1/\varepsilon)}{b\log b}
\left(\int_0^1\phi(x)\,dx-\phi(1)\right)
+o_{b,\phi}(\varepsilon\log(1/\varepsilon)).
\]

Moreover, the probability total-variation distance has the **sharp asymptotic**

\[
\sup_{B\subset[0,1]\ \mathrm{Borel}}|\mu_\beta(B)-\operatorname{Leb}(B)|
\sim\frac{\varepsilon\log(1/\varepsilon)}{b\log b}.
\]

In particular, the invariant-state mean satisfies

\[
\int_0^1x\,d\mu_\beta(x)-\tfrac12
\sim-\frac{\varepsilon\log(1/\varepsilon)}{2b\log b}.
\]

## Assumptions and scope

The integer \(b\) is fixed, \(\beta\in(b-1,b)\), and the limit is only from **below**. Lebesgue probability is invariant at \(\beta=b\); for noninteger \(\beta\) use the unique absolutely continuous invariant probability of the greedy \(\beta\)-transformation. The Dirac mass \(\delta_1\) belongs to the compactification \([0,1]\), even though the map is defined on \([0,1)\). Weak convergence is tested against continuous functions on that compact interval; it is not convergence in total variation to a measure containing a Dirac atom.

## Proof

**1. Invariant density and a positive defect.** Put \(a_0=1\) and recursively \(a_{n+1}=\beta a_n-\lfloor\beta a_n\rfloor\). Parry's explicit formula gives an unnormalized invariant density

\[
w_\beta(x)=\sum_{n=0}^{\infty}\beta^{-n}\mathbf1_{[0,a_n)}(x),
\quad Z_\beta=\int_0^1w_\beta(x)\,dx
=\sum_{n=0}^{\infty}\beta^{-n}a_n,
\quad d\mu_\beta=\frac{w_\beta(x)}{Z_\beta}\,dx.
\]

For completeness, the transfer operator maps \(\mathbf1_{[0,a_n)}\) to \(\beta^{-1}(d_n+\mathbf1_{[0,a_{n+1})})\), where \(d_n=\lfloor\beta a_n\rfloor\). The expansion identity \(\sum_{n\ge0}\beta^{-n-1}d_n=1\) (obtained by telescoping the recursion) then proves invariance term by term. The classical uniqueness of the absolutely continuous invariant probability identifies the normalized measure.

Set

\[
S_\beta=\frac{\beta}{\beta-1},\qquad
v_\beta(x)=\sum_{n=1}^{\infty}\beta^{-n}\mathbf1_{[a_n,1)}(x),\qquad
d_\beta=\int_0^1v_\beta(x)\,dx
=\sum_{n=1}^{\infty}\beta^{-n}(1-a_n).
\]

Almost everywhere, \(w_\beta=S_\beta-v_\beta\), \(Z_\beta=S_\beta-d_\beta\), and therefore the **exact signed density identity** is

\[
d\mu_\beta-dx=\frac{d_\beta-v_\beta(x)}{S_\beta-d_\beta}\,dx.
\tag{1}
\]

**2. A logarithmically long maximal-digit block.** Write \(\varepsilon=b-\beta\). As long as the consecutive digits of the orbit of \(1\) equal \(b-1\), we have \(a_n=1-\Delta_n\), where

\[
\Delta_n=\frac{\varepsilon(\beta^n-1)}{\beta-1}.
\]

The digit \(b-1\) is admissible at the preceding step exactly when \(\Delta_n\le1\). Consequently the initial maximal block has length

\[
m_\beta=\left\lfloor\log_\beta\left(1+\frac{\beta-1}{\varepsilon}\right)\right\rfloor
=\frac{\log(1/\varepsilon)}{\log b}+O_b(1),
\]

and the displayed formula for \(a_n\) is valid for every \(0\le n\le m_\beta\). This assertion includes the finite-expansion boundary where \(\Delta_{m_\beta}=1\). In particular \(\beta^{-m_\beta}=O_b(\varepsilon)\). Split the nonnegative defect mass at this time:

\[
\begin{aligned}
d_\beta
&=\sum_{n=1}^{m_\beta}\beta^{-n}\Delta_n
+\sum_{n>m_\beta}\beta^{-n}(1-a_n)\\
&=\frac{\varepsilon}{\beta-1}\sum_{n=1}^{m_\beta}(1-\beta^{-n})+O_b(\varepsilon)\\
&=\frac{\varepsilon\log(1/\varepsilon)}{(b-1)\log b}+O_b(\varepsilon).
\end{aligned}
\tag{2}
\]

The tail estimate only uses \(0\le a_n<1\); no assumption about later digit itineraries is necessary. Also \(S_\beta-d_\beta\to b/(b-1)\).

**3. Localization of the defect at the right endpoint.** Fix \(\eta\in(0,1)\). For \(x\le1-\eta\), a term of \(v_\beta(x)\) from \(n\le m_\beta\) can occur only when \(\Delta_n\ge\eta\). This forces \(\beta^n\ge 1+\eta(\beta-1)/\varepsilon\), and its remaining geometric weight is bounded by \(O_{b,\eta}(\varepsilon)\). The entire tail \(n>m_\beta\) has weight \(O_b(\varepsilon)\). Thus

\[
\sup_{0\le x\le1-\eta}v_\beta(x)=O_{b,\eta}(\varepsilon).
\tag{3}
\]

Together with (2) and nonnegativity, this proves the finite-measure weak limit

\[
\frac{v_\beta(x)\,dx}{\varepsilon\log(1/\varepsilon)}
\ \xrightarrow{\;\mathrm{weak}\;}\
\frac{\delta_1}{(b-1)\log b}.
\tag{4}
\]

Substitute (2) and (4) into (1), using the normalization limit; the asserted signed weak limit follows. Choosing \(\phi(x)=x\) yields the mean coefficient.

**4. Exact total-variation coefficient.** The difference of the two probability densities in (1) integrates to zero. Accordingly,

\[
\sup_B|\mu_\beta(B)-\operatorname{Leb}(B)|
=\frac1{S_\beta-d_\beta}\int_0^1(d_\beta-v_\beta(x))_+\,dx
\le\frac{d_\beta}{S_\beta-d_\beta}.
\]

For every fixed \(\eta>0\), (3) implies \(v_\beta(x)\le C_{b,\eta}\varepsilon=o(d_\beta)\) on \([0,1-\eta]\). The same integral is therefore at least \((1-\eta)(d_\beta-O_{b,\eta}(\varepsilon))\). Divide by \(d_\beta\), let \(\varepsilon\downarrow0\), and then \(\eta\downarrow0\). The upper and lower limits coincide, and (2) gives the coefficient \(1/(b\log b)\).

## Verification

The accompanying self-contained `verify.py` uses high-precision decimal arithmetic to compute the Parry series for three integer limits \(b\in\{2,3,5\}\), with gaps \(10^{-5},10^{-10},10^{-20},10^{-35}\). It independently integrates the explicit step density to obtain the mean and the positive-part total variation, and checks convergence toward the respective analytical coefficients. It returns `VERIFY_OK`. These finite tests are corroboration, not proof of the universal asymptotics; the proof is the geometric maximal-digit block and the endpoint localization estimates above.

## Relationship to prior work

Rényi introduced \(\beta\)-transformations; Gelfond and Parry obtained the invariant-density formula on which step 1 rests. Góra later studied explicit densities and monotonicity for generalized \(\beta\)-maps. Keller's logarithmic upper stability scale for piecewise expanding families is discussed in Baladi's 2014 review; the latter also exhibits non-differentiable responses in other families. Those sources supply existence, density formulas, or general stability phenomena. The claim here is the **explicit all-integer one-sided signed limit, its endpoint Dirac coefficient, and the matching exact total-variation coefficient**. Neither a general logarithmic upper bound nor the Parry density formula alone states those limits; the present proof supplies the additional orbit-cutoff and localization analysis.

## Limitations

This is a one-sided parameter result at positive integer bases. No right-hand asymptotic, differentiability within noninteger parameter intervals, or convergence in total variation of the *rescaled signed measures* is asserted. A classical density formula and a logarithmic order bound are prior art; historical priority of the sharp coefficients remains subject to comprehensive archival checking. The 2007 source on generalized \(\beta\)-map invariant densities could not be inspected in full. The result concerns the deterministic greedy transformation, not random \(\beta\)-transformations or invariant measures common to two unrelated bases.

## References

1. A. Rényi, *Representations for real numbers and their ergodic properties*, Acta Math. Acad. Sci. Hungar. 8 (1957), 477–493.
2. W. Parry, *On the \(\beta\)-expansions of real numbers*, Acta Math. Acad. Sci. Hungar. 11 (1960), 401–416.
3. P. Góra, *Invariant densities for generalized \(\beta\)-maps*, Ergodic Theory Dynam. Systems 27 (2007), 1583–1598, DOI:10.1017/S0143385707000053.
4. V. Baladi, *Linear Response, Or Else*, arXiv:1408.2937v1, 13 August 2014, especially Section 4.1.
5. G. Brown and Q. Yin, *\(\beta\)-transformation, natural extension and invariant measure*, Ergodic Theory Dynam. Systems 20 (2000), 1271–1285, DOI:10.1017/S0143385700000699.
