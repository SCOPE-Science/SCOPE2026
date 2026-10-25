# Two separated elasticity turning points in a rare–common species–area model

## Finding

Let two species occupy a planar habitat through independent homogeneous Poisson point processes of respective intensities \(1\) and \(\varepsilon\), with \(0<\varepsilon<1\). For a surveyed region of area \(x>0\), let its expected observed richness and local log–log species–area slope be
\[
 S_\varepsilon(x)=2-e^{-x}-e^{-\varepsilon x},\qquad
 z_\varepsilon(x)=\frac{x(e^{-x}+\varepsilon e^{-\varepsilon x})}{2-e^{-x}-e^{-\varepsilon x}}.
\]
There exists \(\varepsilon _0>0\) such that, for every \(0<\varepsilon<\varepsilon _0\), the function \(z_\varepsilon\) has **exactly two critical points** in \((0,\infty)\): a strict local minimum at \(x_-(\varepsilon)\), followed by a strict local maximum at \(x_+(\varepsilon)\). Its derivative has signs negative, positive, negative on the three successive intervals. With \(L=\log(1/\varepsilon)\), the two distinct survey-area scales and their slope values obey
\[
\begin{aligned}
 x_-(\varepsilon)&=L+\log L+o(1),\\
 z_\varepsilon(x_-)&=\varepsilon\bigl(L+\log L+1+o(1)\bigr),\\
 \varepsilon x_+(\varepsilon)&\longrightarrow y_*,\\
 z_\varepsilon(x_+)&\longrightarrow1-y_*.
\end{aligned}
\]
Here \(y_*\in(0,1)\) is the unique solution of \(2(1-y)=e^{-y}\), namely
\[
 y_*=1+W_0(-1/(2e))=0.7680390470134656\ldots,
 \qquad1-y_*=0.2319609529865344\ldots .
\]
Thus a very rare second species produces a secondary, nonvanishing local peak in the effective species–area exponent at an area of order \(1/\varepsilon\), after the exponent first drops to a logarithmically small valley. This **does not** assert that the secondary peak exceeds the small-area limiting slope \(1\).

## Assumptions and scope

An observation detects a species exactly when its independent Poisson point process has at least one point in a sampled region. The processes are stationary and spatially homogeneous, and only the region's area matters; a region need not have any particular shape. Richness means the **expected number** of the two species present, not realized richness and not a power-law fit over a finite range. The local exponent means \(d\log S_\varepsilon/d\log x\), and intensities may be rescaled so the common species has intensity one. All assertions about two critical points concern the sufficiently small, strictly positive rare-to-common intensity ratio, not arbitrary ratios.

## Proof

**Step 1: a sign identity.** Write \(p=e^{-x}\), \(q=e^{-\varepsilon x}\), \(y=\varepsilon x\), \(S=2-p-q\), \(P=p+\varepsilon q=S'\), and \(Q=p+\varepsilon^2q=-S''\). Direct differentiation gives
\[
 z'_\varepsilon(x)=\frac{H_\varepsilon(x)}{S^2},\quad
 H_\varepsilon=SP-x(SQ+P^2).
\]
Algebraically this numerator is exactly
\[
\begin{aligned}
 H_\varepsilon(x)={}&\varepsilon q\,[2(1-y)-q]\\
 &+p\,[(2-q)(1-x)-\varepsilon q(1+(2-\varepsilon)x)]-p^2.
\end{aligned}
\tag{1}
\]
The denominator is strictly positive. Hence it suffices to prove that expression (1) has exactly two positive zeros, with signs \(-,+,-\).

**Step 2: the early interval.** Put \(L=\log(1/\varepsilon)\) and \(t_\varepsilon=L+\log L\). On any fixed interval containing \([0,2]\), the slope converges in \(C^1\), including its continuous extension at zero, to \(z_0(x)=x/(e^x-1)\). This limiting slope has a strictly negative derivative throughout \([0,2]\), the derivative at zero being \(-1/2\). Therefore \(z'_\varepsilon<0\) on \((0,2]\) for small enough \(\varepsilon\).

For \(x\ge2\), the bracket multiplying \(p\) in (1) is no greater than \(1-x\); the first term in (1) is no greater than \(2\varepsilon\). Thus
\[
 H_\varepsilon(x)\le 2\varepsilon-(x-1)e^{-x}.
\tag{2}
\]
Since \((x-1)e^{-x}\) decreases on \([2,\infty)\), and \((t_\varepsilon-A-1)e^{-(t_\varepsilon-A)}=\varepsilon e^A(1+o(1))\), every fixed sufficiently large \(A\) makes \(H_\varepsilon<0\) throughout \([2,t_\varepsilon-A]\).

For each bounded real \(u\), substitution \(x=t_\varepsilon+u\) in (1) gives the locally uniform \(C^1\) limits
\[
 \frac{H_\varepsilon(t_\varepsilon+u)}{\varepsilon}\longrightarrow1-e^{-u},
 \qquad
 \frac{H'_\varepsilon(t_\varepsilon+u)}{\varepsilon}\longrightarrow e^{-u}>0.
\tag{3}
\]
Consequently there is exactly one simple zero in \([t_\varepsilon-A,t_\varepsilon+A]\), at \(t_\varepsilon+o(1)\), and the sign crosses from negative to positive.

**Step 3: exclude extra middle and late zeros.** The limiting late-scale numerator is
\[
 \frac{H_\varepsilon(y/\varepsilon)}{\varepsilon}
 \longrightarrow h(y):=e^{-y}[2(1-y)-e^{-y}]
\tag{4}
\]
locally in \(C^1\) on \((0,\infty)\). The bracket \(2(1-y)-e^{-y}\) is strictly decreasing for \(y>0\), starts at one, and is negative at one; hence its unique zero \(y_*\) is simple and \(h'(y_*)<0\). For a small fixed \(\delta>0\), (4) implies exactly one late simple zero in \([(y_*-\delta)/\varepsilon,(y_*+\delta)/\varepsilon]\), crossing from positive to negative.

It remains to control the two long intervals that compact convergence does not cover. On \([t_\varepsilon+A,(y_*-\delta)/\varepsilon]\), the first term \(\varepsilon q[2(1-y)-q]\) in (1) is bounded below by a positive constant times \(\varepsilon\), independent of small \(\varepsilon\). The magnitude of the sum of the remaining terms is bounded by \(C(1+x)e^{-x}\), and this is at most \(C'\varepsilon e^{-A}\) since \(x\ge t_\varepsilon+A\). Choose \(A\) sufficiently large; then \(H_\varepsilon>0\) across this entire interval.

On \([ (y_*+\delta)/\varepsilon,\infty)\), the first term is negative and has absolute magnitude at least \(c_\delta\varepsilon e^{-\varepsilon x}(1+\varepsilon x)\). The other terms are bounded by \(C(1+x)e^{-x}\), whose ratio to this lower bound is at most
\[
 C'\varepsilon^{-2}e^{-(1-\varepsilon)(y_*+\delta)/\varepsilon}=o(1).
\]
Thus \(H_\varepsilon<0\) throughout the remaining late tail. All intervals together establish exactly two critical points and the derivative-sign pattern.

**Step 4: critical locations and heights.** Equation (3) implies \(x_-=t_\varepsilon+o(1)\). At this point \(p=(\varepsilon/L)(1+o(1))\), \(q=1+O(\varepsilon L)\), and \(S=1+O(\varepsilon L)\); substitution into \(z=x(p+\varepsilon q)/S\) yields
\[
 z_\varepsilon(x_-)=\varepsilon(L+\log L+1+o(1)).
\]
Here the displayed \(+1\) follows because \(p/\varepsilon=1/L+o(1/L)\), whereas the \(q\)- and denominator corrections are negligible at the specified additive precision. For \(x=y/\varepsilon\), the slope converges in \(C^1\) on compact positive \(y\)-intervals to \(g(y)=ye^{-y}/(2-e^{-y})\). Its derivative has the sign of \(2(1-y)-e^{-y}\), so the unique late point obeys \(\varepsilon x_+\to y_*\) and its height tends to \(g(y_*)=1-y_*\). This completes the proof.

## Verification

The accompanying `verify.py` uses only Python's standard library. It independently evaluates both algebraically equivalent derivative numerators, locates the two sign changes by bisection for five small ratios, compares the logarithmic valley location and the rescaled secondary peak, and tests the identity and derivative by 2,000 reproducible random choices. Run `python3 verify.py`. The program checks finite instances; the sign controls in the proof, not finite sampling, establish the universal theorem.

For example, at \(\varepsilon=10^{-3}\), the computed minimum is at \(x_-=9.018965838356\ldots\), with local exponent \(0.009942048048\ldots\); the secondary maximum is at \(x_+=768.039047013466\ldots\), with local exponent \(0.231960952987\ldots\).

## Relationship to prior work

Two-species species–area curves with markedly unequal abundance, their inflected shapes, and the relevance of common versus rare species were **already demonstrated qualitatively** by Tjørve, Kunin, Polce and Calf Tjørve (2008). Turner and Tjørve (2005) likewise study scale dependence of species–area relationships. The novelty asserted here is narrower: a proved **exactly-two-critical-points classification in the rare-species limit**, the unexpected early scale \(\log(1/\varepsilon)+\log\log(1/\varepsilon)\), and a universal late-area peak height and location for the continuous independent-Poisson version. Neither the generic Poisson occupancy identity nor the qualitative possibility of nonmonotone local slopes is claimed as new.

The 2008 paper's complete accessible article, including its two-species examples and discussion, and the complete accessible Turner–Tjørve article were compared with the stated theorem. No explicit corresponding rare-intensity two-scale theorem was identified in those texts. The original mathematical random-placement work of Coleman (1981) and the later Coleman et al. (1982) article remain possible broader sources; their complete full texts were not available for this comparison. That leaves a substantive but presently unresolved historical-coverage risk. A general theorem on elasticity of mixtures of exponential saturations could also imply the formulas without using ecological terminology.

## Limitations

The result is asymptotic as the rare species becomes arbitrarily rare and supplies no numerical, optimal, or sharp value of the smallness threshold \(\varepsilon_0\). It concerns only two independent homogeneous species and expected richness; it does not prove the shape of empirical species–area curves under aggregation, interactions, sampling without replacement, heterogeneous intensities, or fixed-area finite populations. The secondary local peak height is less than the limiting slope at zero. Priority of the precise mathematical statements has not been independently verified against every historical source.

## References

1. Tjørve, E., Kunin, W. E., Polce, C., and Calf Tjørve, K. M. (2008). Species–area relationship: separating the effects of species abundance and spatial distribution. *Journal of Ecology* 96, 1141–1151. DOI: 10.1111/j.1365-2745.2008.01433.x. Online version-of-record date recorded as 24 September 2008.
2. Turner, W. R., and Tjørve, E. (2005). Scale-dependence in species–area relationships. *Ecography* 28. DOI: 10.1111/j.2005.0906-7590.04273.x.
3. Coleman, B. D. (1981). On random placement and species–area relations. *Mathematical Biosciences*. DOI: 10.1016/0025-5564(81)90086-9. Full text not examined.
4. Coleman, B. D., Mares, M. A., Willig, M. R., and Hsieh, Y.-H. (1982). Randomness, area, and species richness. *Ecology* 63. DOI: 10.2307/1937249. Full text not examined.
