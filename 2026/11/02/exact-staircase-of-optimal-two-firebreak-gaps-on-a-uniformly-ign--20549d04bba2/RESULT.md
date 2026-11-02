# Exact staircase of optimal two-firebreak gaps on a uniformly ignited cycle

## Finding

For every integer \(N\ge4\), consider two barriers obtained by deleting distinct edges from a cycle of \(N\) habitat patches. Under independent one-season ignition probability \(p\in(0,1)\) per patch and complete within-component fire spread, every allowable barrier gap is the **unique expected-burn minimizer** on a nonempty, explicitly specified interval of \(q=1-p\). These intervals follow the strict sequence from adjacent barriers at high ignition risk to equally spaced barriers at low ignition risk.

Put \(m=\lfloor N/2\rfloor\). For \(1\le j\le m\), let the two resulting connected components have \(j\) and \(N-j\) patches. The expected number of burned patches is
\[
 B_j(q)=N-jq^j-(N-j)q^{N-j}.
\]
For each \(1\le j<m\), define \(r_j\) to be the unique root in \((0,1)\) of
\[
 \sum_{a=1}^{N-2j-2}r_j^a+(N-j)r_j^{N-2j-1}=j,
\]
where an empty sum is zero. These thresholds satisfy
\[
 0<r_1<r_2<\cdots<r_{m-1}<1.
\]
With \(r_0=0\), \(r_m=1\), the **unique** optimum for \(r_{j-1}<q<r_j\) is gap \(j\). At \(q=r_j\), precisely gaps \(j\) and \(j+1\) tie. Hence all \(m\) geometries occur as unique optima, with no skipped geometry and no three-way tie.

For \(N=8\), the thresholds are approximately \(0.469138898665\), \(0.569240819317\), and exactly \(3/5\). The respective unique optimal gaps at \(q=2/5,1/2,7/12,3/4\) are \(1,2,3,4\). At \(q=3/4\), equally spaced cuts have expected burn \(175/32\) versus \(103475/16384\) for adjacent cuts.

## Assumptions and scope

The landscape is exactly the undirected cycle graph \(C_N\) with \(N\ge4\) equally weighted patches. Two different edges are removed before the season; no other protective intervention is allowed. The deleted edges completely block spread and all remaining edges transmit surely. In the season each patch has an independent intrinsic ignition indicator with common probability \(p\in(0,1)\). Given at least one ignition in a connected component, all its patches burn. The objective is expected total patch count burned, not peak intensity, time to burn, or suppression cost. Rotation and reflection of barrier locations are identified because all patches and edges are homogeneous.

## Proof

**Expectation.** The two deleted edges partition the cycle into paths of lengths \(j\) and \(N-j\). A component of size \(s\) experiences no ignition with probability \(q^s\) and otherwise burns completely. Thus the expected saved count is
\[
 H_j(q)=jq^j+(N-j)q^{N-j},
\]
so minimizing \(B_j\) is equivalent to maximizing \(H_j\).

**Adjacent crossings.** For every \(1\le j<m\), direct expansion and geometric summation give the *exact factorization*
\[
 H_{j+1}(q)-H_j(q)=q^j(1-q)\left[\sum_{a=1}^{N-2j-2}q^a+(N-j)q^{N-2j-1}-j\right].
\]
The expression in square brackets has negative limit \(-j\) at \(q=0\), and is strictly increasing on \((0,1)\), since every displayed positive power has a positive coefficient. At \(q=1\) it equals \(N-2j-2+(N-j)-j=2N-4j-2>0\), because \(j<m\). There is therefore one simple crossing \(r_j\): \(H_{j+1}<H_j\) for \(q<r_j\), with the reverse inequality for \(q>r_j\).

**No valleys or triple ties.** Fix \(q\in(0,1)\), put \(t=-\log q>0\), and extend \(H_j\) to real \(x\in[0,N/2]\) by \(h(x)=xq^x+(N-x)q^{N-x}\). Writing \(y=N/2-x\), \(z=ty\), one obtains
\[
 h(x)=e^{-Nt/2}\bigl[N\cosh(ty)-2y\sinh(ty)\bigr].
\]
For \(y>0\), its derivative with respect to \(y\) has the sign of
\[
 \frac{Nt}{2}-1-z\coth z.
\]
The function \(z\coth z\) is strictly increasing on \((0,\infty)\), from limit \(1\), since its derivative has numerator \(\sinh z\cosh z-z>0\). At the endpoint \(y=N/2\), the displayed sign is strictly negative. It follows that \(h(x)\) is either strictly increasing throughout \([0,N/2]\), or strictly increases and then strictly decreases, with a unique interior maximum. Consequently the sampled sequence \(H_1,\ldots,H_m\) has no strict valley and cannot have three consecutive equal values.

**Ordering and globality.** If \(r_{j+1}<r_j\), select \(q\) between these roots. The adjacent-crossing signs imply \(H_j>H_{j+1}<H_{j+2}\), contradicting the no-valley conclusion. If \(r_{j+1}=r_j\), then three consecutive \(H\)'s are equal, also impossible. Thus \(r_1<\cdots<r_{m-1}\). For \(r_{j-1}<q<r_j\), the crossing signs, with ordered roots, imply
\[
 H_1<\cdots<H_j>\cdots>H_m.
\]
At each \(r_j\), exactly the two adjacent terms \(H_j,H_{j+1}\) attain the maximum. Therefore all the claimed optimality intervals and ties follow. This also establishes the theorem for the smallest case \(N=4\), for even/odd \(N\), and arbitrarily close to either ignition endpoint (which themselves are excluded).

## Verification

Run the standalone file `check_firebreak.py` using Python 3 from the same directory. It checks the model-based expectation against full ignition-outcome enumeration for \(4\le N\le9\), exact rational adjacent identities through \(N=44\), and ordered threshold/optimality tests through \(N=64\); it also checks four different exact optima at \(N=8\). It reports `PASS: 2968 independent exact/finite checks`. These finite computations supplement, not replace, the proof for all integers \(N\ge4\).

## Relationship to prior work

Spatial arrangement of fuel treatments has been studied with fire-spread geometry (Finney 2001), stochastic/landscape integer programming (Wei, Rideout & Kirsch 2008), simulation-optimization (Rytwinski & Crowe 2010), and heterogeneous-network centrality methods (Russo, Russo & Siettos 2015/2016). Those approaches motivate the importance of arrangement but do not, in the material inspected, give this complete analytical staircase for **exactly two cycle-edge barriers, exchangeable independent ignitions, and deterministic within-component propagation**. The 2015 research preprint has verified initial public posting September 14, 2015. Related general partition inequalities were assessed; \(xq^x\) changes curvature on the relevant domain, so elementary global convex/concave balancing alone does not cover all regimes. Historical priority is provisional because some plausible full texts were inaccessible.

## Limitations

The theorem assumes a uniformly weighted, finite ring; independent homogeneous ignition; invulnerable barriers; complete spread inside components; and exactly two removed edges. It does not model wind, embers jumping breaks, fire intensity, delayed suppression, correlated ignitions, heterogeneous fuel, or geometry beyond a cycle. The thresholds are for expected affected patch count, not a guarantee about one season. Numerical checking is finite and does not independently certify historical novelty.

## References

1. M. A. Finney, “Design of Regular Landscape Fuel Treatment Patterns for Modifying Fire Growth and Behavior,” *Forest Science* 47 (2001), 219–228, DOI: 10.1093/forestscience/47.2.219. Full lawful text: https://www.fs.usda.gov/rm/pubs/rmrs_gtr292/2001_finney.pdf.
2. Y. Wei, D. Rideout and A. Kirsch, “An Optimization Model for Locating Fuel Treatments Across a Landscape to Reduce Expected Fire Losses,” *Canadian Journal of Forest Research* 38 (2008), 868–877, DOI: 10.1139/X07-162.
3. A. Rytwinski and K. A. Crowe, “A Simulation-Optimization Model for Selecting the Location of Fuel-Breaks to Minimize Expected Losses from Forest Fires,” *Forest Ecology and Management* 260 (2010), 1–11, DOI: 10.1016/j.foreco.2010.03.013.
4. L. Russo, P. Russo and C. I. Siettos, “A Complex Network Theory Approach for the Spatial Distribution of Fire Breaks in Heterogeneous Forest Landscapes for the Control of Wildland Fires,” arXiv:1509.04065v1, first posted September 14, 2015, https://arxiv.org/abs/1509.04065.
5. F. K. Hwang and U. G. Rothblum, “Partition-Optimization with Schur Convex Sum Objective Functions,” *SIAM Journal on Discrete Mathematics*, DOI: 10.1137/S0895480198347167 (general mathematical comparison, not a wildfire model).
