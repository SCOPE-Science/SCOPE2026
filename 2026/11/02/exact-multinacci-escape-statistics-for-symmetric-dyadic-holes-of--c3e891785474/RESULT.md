# Exact multinacci escape statistics for symmetric dyadic holes of the negative-doubling map

## Finding

Let \(T:[0,1]\setminus\{1/2\}\to[0,1]\) be the negative-doubling map
\[
T(x)=\begin{cases}1-2x,&0\le x<1/2,\\ 2-2x,&1/2<x\le1.\end{cases}
\]
For each integer \(m\ge2\), remove the open **symmetric dyadic critical hole**
\[
H_m=\left(\frac12-2^{-m},\frac12+2^{-m}\right).
\]
Let \(\tau_m(x)=\inf\{j\ge0:T^j(x)\in H_m\}\) with \(\inf\varnothing=\infty\), where the finitely or countably many points with a critical or boundary ambiguity may be assigned arbitrarily: they are Lebesgue-null. Set \(r=m-2\), and define \(b_{r,\ell}=0\) for \(\ell<0\), \(b_{r,0}=1\), and for all integers \(\ell\ge1\),
\[
b_{r,\ell}=1+\sum_{j=1}^{r}b_{r,\ell-j}.
\]
(For \(r=0\), this gives \(b_{0,\ell}=1\).) With \(\mathbb P\) denoting normalized Lebesgue measure on \([0,1]\), the **exact finite-time first-entry survival law**, for every integer \(t\ge1\), is
\[
\boxed{\mathbb P(\tau_m\ge t)=\frac{b_{r,t+r}}{2^{t+r}}.}
\]
Moreover the generating function and the exact unconditional mean are
\[
\boxed{\sum_{\ell\ge0}b_{r,\ell}z^\ell
=\frac{1}{(1-z)\left(1-\sum_{j=1}^r z^j\right)},\qquad
\mathbb E\tau_m=2^{m-1}-m+1.}
\]
The expectation is finite, so \(\tau_m<\infty\) almost surely. For \(m=2,3\), the survival exponent is \(\log2\). For each \(m\ge4\), let \(\lambda_m\in(1,2)\) be the unique positive root greater than one of
\[
\lambda_m^{m-2}=\lambda_m^{m-3}+\cdots+\lambda_m+1.
\]
Then the exact Lebesgue escape rate is
\[
\boxed{\gamma_m=\lim_{t\to\infty}-\frac1t\log\mathbb P(\tau_m\ge t)
=\log\frac2{\lambda_m},\quad m\ge4.}
\]
The infinite-time survivor has topological entropy \(\log\lambda_m\) and Hausdorff dimension \(\log\lambda_m/\log2\) for \(m\ge4\); both are zero for \(m=2,3\). Thus \(m=4\) is the first dyadic refinement in this family with positive survivor entropy. The small-hole limit satisfies
\[
\gamma_m=2^{1-m}+O\!\left(m4^{-m}\right)\quad(m\to\infty).
\]
The core contribution is the explicit **all-resolution finite-time recurrence and mean first-entry law**; constant-slope entropy/dimension relations are standard consequences and are not claimed independently new.

## Assumptions and scope

Time is discrete. The map is defined on both open monotonicity branches; any choice at \(1/2\) and at precritical or hole-boundary points changes none of the Lebesgue probabilities. The hole is open, centered exactly at the branch discontinuity, and has dyadic half-width \(2^{-m}\) with **every integer** \(m\ge2\). Initial conditions have uniform Lebesgue distribution. The formula is not asserted for asymmetric holes, non-dyadic widths, nonlinear Lorenz branches, nonuniform starting distributions, or stochastic disturbances.

For entropy/dimension, retain whichever endpoint completion makes the compact invariant survivor definition convenient: any discrepancy lies in a countable precritical/boundary set and does not change these invariants. The finite-time statements concern exact Lebesgue probabilities and need no completion convention.

## Proof

**1. Equal-measure branch coding.** Each monotonicity branch maps its open domain onto \((0,1)\) with slope of magnitude \(2\). For every length \(n\ge1\), every binary branch itinerary \(s_0s_1\cdots s_{n-1}\) determines one interval of length \(2^{-n}\), up to endpoints. Under Lebesgue measure, branch symbols therefore form a fair Bernoulli sequence. Reflection \(x\mapsto1-x\) complements the branch symbols.

**2. Exactly two forbidden words.** The two depth-\(m\) cylinders adjacent to the discontinuity are precisely the two halves of \(H_m\). Approaching \(1/2\) from the left, the next branch images alternate near \(0,1,0,1,\ldots\), so its depth-\(m\) word begins \(00101\ldots\). Reflection gives the complement \(11010\ldots\) on the right. More explicitly, the two forbidden words \(A_m,B_m\) of length \(m\) have \(s_0=s_1\) and \(s_{j+1}\ne s_j\) for every \(1\le j\le m-2\), with the initial common symbol respectively \(0\) and \(1\). This also covers \(m=2\), when the forbidden words are \(00,11\). A visit to \(H_m\) at time \(j\) is equivalent, except on null cylinder boundaries, to the block of symbols at positions \(j,\ldots,j+m-1\) being either \(A_m\) or \(B_m\).

**3. A binary-difference recoding and an exact recurrence.** Given any \(n\ge1\) branch symbols, let \(d_j=1\) when \(s_j=s_{j+1}\) and \(d_j=0\) otherwise, for \(0\le j<n-1\). The map from \(s_0s_1\cdots s_{n-1}\) to \((s_0,d_0,\ldots,d_{n-2})\) is bijective: recover each subsequent bit from the previous bit and the equality indicator. The two forbidden words **together** become the one forbidden difference word \(10^r\), of length \(r+1=m-1\). Let \(b_{r,\ell}\) count length-\(\ell\) binary difference words avoiding \(10^r\). Thus the number of admissible branch strings of length \(n\ge1\) is exactly \(a_{m,n}=2b_{r,n-1}\).

Any admissible difference word of length \(\ell\) is either all zeros (one choice), or has a last \(1\) followed by exactly \(j\) zeros for one \(0\le j<r\). The part preceding that last \(1\) is any shorter admissible word. This gives \(b_{r,\ell}=1+\sum_{j=1}^r b_{r,\ell-j}\), with the stated initial and negative-index conventions. When \(r=0\), every \(1\) is forbidden and the unique word is all zeros, so the same recurrence holds with an empty sum. Summing over \(\ell\ge0\) yields the displayed rational generating function, including \(r=0\).

**4. Exact first-entry law and mean.** Having \(\tau_m\ge t\) means avoiding the hole at each time \(0,\ldots,t-1\). Exactly \(t+m-1\) branch symbols are required to decide those \(t\) blocks. Their number is \(2b_{r,t+m-2}\), and each has Lebesgue measure \(2^{-(t+m-1)}\). Since \(r=m-2\), the probability is \(b_{r,t+r}/2^{t+r}\). The tail-sum identity for a nonnegative integer random variable gives
\[
\mathbb E\tau_m=\sum_{t\ge1}\mathbb P(\tau_m\ge t)
=\sum_{\ell\ge r+1}\frac{b_{r,\ell}}{2^\ell}.
\]
The shortest forbidden difference word has length \(r+1\), hence \(b_{r,\ell}=2^\ell\) for \(0\le\ell\le r\). The generating function at \(z=1/2\) has value \(2^{r+1}\): indeed \(\sum_{j=1}^r2^{-j}=1-2^{-r}\), even when \(r=0\). Subtracting the first \(r+1\) unit summands gives \(2^{r+1}-(r+1)=2^{m-1}-m+1\). The finite expectation forces almost-sure eventual entry.

**5. Escape, entropy and dimension.** For \(r=0\), \(b_{0,\ell}=1\); for \(r=1\), \(b_{1,\ell}=\ell+1\), so both exponential growth rates equal one. For \(r\ge2\), the recurrence is a positive forcing of the primitive \(r\)-step Fibonacci transfer matrix. Its Perron eigenvalue is the unique root \(\lambda_m\in(1,2)\) of the displayed equation, and \(\lim_{\ell\to\infty}\ell^{-1}\log b_{r,\ell}=\log\lambda_m\). The exact probability then gives \(\gamma_m=\log(2/\lambda_m)\). A uniform-slope graph-directed cylinder covering, with bounded overlaps, gives Hausdorff dimension \(\log\lambda_m/\log2\) and entropy \(\log\lambda_m\); the two-to-one difference coding preserves the exponential word growth. When \(r\le1\), word growth is at most linear and both invariants vanish.

Finally put \(r=m-2\) and \(\delta_r=2-\lambda_m\). Multiplying the characteristic equation by \(\lambda_m-1\) shows \(\delta_r(2-\delta_r)^r=1\). The root in \((0,1)\) satisfies \(\delta_r=2^{-r}+O(r4^{-r})\), by expansion of \((1-\delta_r/2)^{-r}\) and the elementary bounds \(2^{-r}<\delta_r<2^{1-r}\) for all \(r\ge2\). Therefore \(\log(2/\lambda_m)=-\log(1-\delta_r/2)=2^{-r-1}+O(r4^{-r})=2^{1-m}+O(m4^{-m})\), as claimed.

## Verification

The standalone standard-library Python file `verify.py` independently enumerates all binary length-\(n\) strings up to \(n=14\) for each \(2\le m\le8\), checks the recurrence against exhaustive forbidden-word exclusion, constructs every depth-\(m\) interval by exact rational arithmetic, and confirms that the two central cylinders have the asserted itinerary words. It also checks first-entry survival directly by rational orbit iteration for \(2\le m\le6\) and \(1\le t\le6\). Running `python verify.py` completed with PASS. These finite checks stress-test the proof but do not certify the infinite quantifiers, which are settled by the preceding bijection and recurrence argument.

## Relationship to prior work

Ding, Steiner and Sun [1] establish a general kneading/entropy/dimension theory for open negative-doubling and decreasing Lorenz maps. Their theorems imply the standard relation between entropy and Hausdorff dimension, but do not tabulate this all-resolution **finite-time survival generating function and unconditional exact hitting-time expectation**. A separate published dynamical result [2] classifies the eventual-periodic survivor regime for all symmetric holes with left endpoint at most \(2/5\); the present first two dyadic holes are in that zero-entropy regime, while every dyadic level starting at \(m=4\) lies above it. That work studies periodic orbit spectra and zeta functions, not the all-time Lebesgue escape distribution for the dyadic family. General compound-pattern waiting-time methods [3,4] can in principle compute finite-state distributions for *any* specified forbidden list. The point here is an explicit uniform closed recurrence and mean for every critical dyadic resolution, obtained via the simple equality-indicator recoding; these general methods are not asserted to be new or invalid. No exhaustive historical-priority claim is made.

## Limitations

The result is an exact family of open piecewise-linear maps, not a theorem about arbitrary Lorenz maps or smooth perturbations. Entropy and Hausdorff dimension are standard graph-directed consequences rather than independent innovations. The listed probability and mean assume initially uniform Lebesgue sampling, and the escape exponent does not describe all finer conditional distributions without the recurrence. Although a classical general pattern-matching algorithm subsumes the **possibility** of computing each fixed-resolution case, the inspected sources did not state the uniform all-\(m\) formula. A different existing closed formula under an equivalent coding would overturn the originality assessment; this remains a historical-priority risk.

## References

[1] Y. Ding, W. Steiner, Y. Sun, *Open dynamical systems in topologically expansive decreasing Lorenz maps*, arXiv:2610.03327v1, first posted 2 October 2026, https://arxiv.org/abs/2610.03327 .

[2] *A three-phase periodic-orbit and zeta trichotomy for symmetric negative-doubling holes*, published published-finding corpus research record, 11 October 2026, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-a-three-phase-periodic-orbit-and-zeta-trichotomy-for-symmetric-n--8027a957802c .

[3] B. C. Johnson, J. C. Fu, *Approximating the distributions of runs and patterns*, Journal of Statistical Distributions and Applications 1, 5 (2014), https://doi.org/10.1186/2195-5832-1-5 .

[4] K. Jin, *Computing the Pattern Waiting Time: A Revisit of the Intuitive Approach*, ISAAC 2016, https://doi.org/10.4230/LIPIcs.ISAAC.2016.39 .
