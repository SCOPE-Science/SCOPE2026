# Eventual ultra-log-concavity of discrete-uniform sample ranges and the sharp six-face transition

## Finding
Let \(m\ge2\) and \(n\ge2\) be integers. For independent uniform \(X_1,\ldots,X_n\) on \(\{0,1,\ldots,m\}\), put \(R_{m,n}=\max_i X_i-\min_i X_i\) and \(p_r=\Pr(R_{m,n}=r)\). A distribution on \(\{0,\ldots,m\}\) is *ultra-log-concave* (ULC) here if \(k p_k^2\ge(k+1)p_{k-1}p_{k+1}\) for every integer \(1\le k<m\).

**Theorem.** For every \(m\ge2\), the range law is **strictly** ULC whenever \(n\ge m^2\). Conversely, for every \(m\ge3\), its range law at \(n=2\) is **not** ULC. For the six-face case \(m=5\), the exact result for every \(n\ge2\) is
\[
R_{5,n}\text{ is ULC}\quad\Longleftrightarrow\quad n\ge4,
\]
with strict inequalities at every interior range value when \(n\ge4\). The sample-size-one point mass is degenerate and is excluded from this nondegenerate classification.

Thus a nonlinear range statistic can acquire strict ULC even though the finite-uniform parent is itself non-ULC; sufficiently many independent observations produce this strong shape property for *every fixed finite alphabet*. The six-face transition is sharp rather than merely asymptotic.

## Assumptions and scope
The sampling is with replacement, independent and identically distributed, uniform on exactly \(m+1\) consecutive integers. Translating the alphabet does not change the range. No claim is made for heterogeneous sampling, arbitrary parent probabilities, nonconsecutive support, or an optimal universal sample-size bound. MSC2020: 60E15.

For integers \(r\ge1\), abbreviate
\[
B_r(n)=(r+1)^n-2r^n+(r-1)^n.
\]
The following exact integer weights are the range probabilities multiplied by \((m+1)^n\):
\[
a_0=m+1,\qquad a_r=(m+1-r)B_r(n)\quad(1\le r\le m),\qquad
p_r=\frac{a_r}{(m+1)^n}.
\]
They have no internal zeros. Consequently, ULC is equivalent to \(D_k=k a_k^2-(k+1)a_{k-1}a_{k+1}\ge0\) for every \(1\le k<m\).

## Proof
**1. Exact masses.** A zero range means that all \(n\) observations equal a single one of the \(m+1\) symbols. For a positive range \(r\), choose its left endpoint in \(m+1-r\) ways; then inclusion–exclusion counts tuples whose entries lie in an interval of \(r+1\) symbols and hit both endpoints. This gives \(B_r(n)\), hence the displayed formula. Summing over disjoint possible ranges counts all \((m+1)^n\) ordered samples.

**2. Every alphabet eventually yields strictly ULC ranges.** Fix \(m\ge2\) and \(n\ge m^2\); in particular \(n\ge4\). For the first interior inequality, note that \(B_1(n)=2^n-2\), and \(B_2(n)=3^n-2\cdot2^n+1<3^n\). For \(n\ge4\),
\[
(2^n-2)^2\ge\frac{49}{64}4^n>2\cdot3^n.
\]
The last strict inequality holds at \(n=4\) since \(196>162\), and its ratio increases geometrically with \(n\). Therefore
\[
a_1^2=m^2(2^n-2)^2>2(m^2-1)B_2(n)=2a_0a_2.
\]
If \(m=2\), this is the only interior inequality.

For \(m\ge3\), consider \(2\le k\le m-1\) and set \(t=m+1-k\ge2\). The elementary inequalities
\[
(k+1)^n\left[1-2\left(\frac{k}{k+1}\right)^n\right]\le B_k(n)\le(k+1)^n
\]
show, since \(B_{k-1}(n),B_{k+1}(n)>0\), that
\[
\frac{B_k(n)^2}{B_{k-1}(n)B_{k+1}(n)}
\ge\left(1+\frac{1}{k(k+2)}\right)^n
\left[1-2\left(\frac{k}{k+1}\right)^n\right]^2.
\]
Here \(k(k+2)\le m^2-1\). Bernoulli's inequality and \(n\ge m^2\) give
\[
\left(1+\frac{1}{k(k+2)}\right)^n\ge1+\frac{n}{m^2-1}>2.
\]
Also \(k/(k+1)\le1-1/m\), hence
\[
\left(\frac{k}{k+1}\right)^n\le(1-1/m)^n<e^{-n/m}\le e^{-m}\le e^{-3}<\frac1{20}.
\]
Consequently \(B_k(n)^2/[B_{k-1}(n)B_{k+1}(n)]>2(9/10)^2=81/50>3/2\ge(k+1)/k\). The linear taper only helps: explicitly,
\[
\frac{a_k^2}{a_{k-1}a_{k+1}}=
\frac{t^2}{t^2-1}\frac{B_k(n)^2}{B_{k-1}(n)B_{k+1}(n)}
>\frac{k+1}{k}.
\]
Thus all ULC inequalities are strict, including those nearest either endpoint, for every \(n\ge m^2\).

**3. Two draws fail for every alphabet with at least four faces.** When \(n=2\), \(a_0=m+1\) and \(a_r=2(m+1-r)\) for \(1\le r\le m\). At the interior index \(k=2\), available when \(m\ge3\),
\[
D_2=2a_2^2-3a_1a_3=-4m^2+8m+8<0\quad(m\ge3).
\]
This witnesses non-ULC without an experiment.

**4. Sharp six-face transition.** Take \(m=5\). At \(n=2\) and \(n=3\), the same interior defect \(D_2\) is respectively \(-52\) and \(-252\); hence both fail. For every integer \(4\le n\le24\), direct exact-integer evaluation of the explicit \(a_r\) gives \(D_k>0\) at **all four** interior indices \(k=1,2,3,4\). The standalone `check.py` evaluates every one of these 84 inequalities and also independently reconstructs the entire range count vector from a dynamic program over sample minima and maxima. All operations are on exact integers; no untested intermediate trial sizes remain. For every \(n\ge25=m^2\), part 2 proves all four inequalities strictly. Therefore the six-face iff classification holds for every \(n\ge2\), completing the proof.

## Verification
Run `python3 check.py` with any Python 3 interpreter. It checks the complete finite gap \(2\le n\le24\), verifies formula counts against an independently formed endpoint-state recursion, checks exact normalization, establishes negative \(D_2\) for \(n=2,3\), and verifies the complete set of strict inequalities for \(4\le n\le24\). The proof, not these finite checks, covers **all** \(n\ge m^2\) and **all** finite alphabets. Additional finite-alphabet checks in the script corroborate but do not replace that proof.

## Relationship to prior work
Badiella, del Castillo and Puig (2023) proved ULC preservation for **individual discrete order statistics**. Their theorem does not imply ULC of \(\max_iX_i-\min_iX_i\): for \(m\ge2\) the discrete-uniform parent itself fails ULC, and the difference of dependent extremes is not an individual order statistic. The weaker ordinary log-concavity of the uniform parent does not settle ULC of the range. The original 2023 article's indexed text covers the one-statistic recursion and the Poisson-underdispersion corollary, not the discrete-uniform range phase transition established here. Puig (2024) surveys mechanisms of underdispersion and order-statistic results; this does not supply the stated range law. Saumard and Wellner (2014) survey ULC and its closure mechanisms, none of which directly handles a difference of dependent extremes. The elementary range-counting identity by itself does not imply the global \(n\ge m^2\) ULC conclusion or the sharp die cutoff.

## Limitations
The \(m^2\) sufficient sample-size bound is deliberately explicit and **not claimed sharp**; for \(m=5\) the exact threshold is much smaller. The result gives ULC, not total positivity of every order, and concerns only a uniform consecutive alphabet. The finite checker is exhaustive for the **stated finite range** \(4\le n\le24\), not an infinite theorem. The relevant publisher and institutional PDF copies were not both fully obtainable, though substantial searchable article text and the stated published theorem were inspected. Unindexed equivalent previous literature remains a possible originality risk.

## References
1. L. Badiella, J. del Castillo and P. Puig, “Ultra log-concavity of discrete order statistics,” *Statistics & Probability Letters* **201** (2023), 109900, DOI: 10.1016/j.spl.2023.109900. First available online 2023-06-26.
2. P. Puig, J. Valero and A. Fernández-Fontelo, “Some mechanisms leading to underdispersion: Old and new proposals,” *Scandinavian Journal of Statistics* **51** (2024), 245–267, DOI: 10.1111/sjos.12677.
3. A. Saumard and J. A. Wellner, “Log-Concavity and Strong Log-Concavity: A Review,” *Statistical Surveys* **8** (2014), 45–114, DOI: 10.1214/14-SS107.
