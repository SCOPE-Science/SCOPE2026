# An exact aftershock echo staircase for three-stage delayed triggering

## Finding

For a single earthquake at time zero, consider the *linear subcritical branching aftershock model* in which each event produces direct descendants with time-lag intensity \(k_m(t)=q\beta^m t^{m-1}e^{-\beta t}/(m-1)!\), for \(t>0\), branching ratio \(0<q<1\), clock scale \(\beta>0\), and Erlang stage count \(m\in\{1,2,3\}\). There are no immigrants after time zero. Let \(G_m(t)\) be the **expected rate of all generations of descendants**, excluding the initiating event.

The first stage gives a strictly decreasing response and the second stage gives exactly one strict local maximum. At three stages, a sharp infinite *echo staircase* occurs: for every integer \(j\geq1\), there is an explicit threshold \(q_j\) such that
\[
N_3(q)=1+\#\{j\geq1:q>q_j\},\qquad 0<q_1<q_2<\cdots<1,
\]
where \(N_3(q)\) is the number of strict local maxima of \(G_3\) for \(t>0\). Thus any fixed subcritical model has finitely many peaks, but their number is unbounded as \(q\uparrow1\). Equality \(q=q_j\) creates a stationary horizontal inflection, **not** an additional maximum. In particular \(m=3\) is the smallest of these integer Erlang stages that admits secondary rate peaks.

The exact thresholds are obtained as follows. Let \(\theta_j\) be the unique solution in \((2\pi j,(2j+1)\pi)\) of
\[
e^{\sqrt3\theta_j}(\cos\theta_j-\sqrt3\sin\theta_j)=1.
\]
Set \(d_j=\sqrt3\sin\theta_j/(e^{\sqrt3\theta_j}-\cos\theta_j)\), then
\[
q_j=\left(\frac{1-d_j}{1+d_j}\right)^3.
\]
In particular, \(q_1=0.9999606018054937259\ldots\) and \(q_2=0.9999999992601499757\ldots\). The thresholds have the geometric asymptotic law
\[
1-q_j\sim3\sqrt3\,e^{-\sqrt3(2\pi j+\pi/6)}.
\]
For instance \(q=99999/100000\) produces exactly two rate peaks under a three-stage kernel, whereas the same branching ratio yields only one peak with a two-stage kernel.

## Assumptions and scope

Each event independently initiates a Poisson process of first-generation aftershocks with deterministic age-dependent intensity \(k_m\). Events reproduce independently with the same law. Since \(\int_0^\infty k_m(t)dt=q<1\), the Poisson branching cluster is almost surely finite and its expected descendant count is \(q/(1-q)\). We study the ensemble mean event-rate response, not individual observed clusters, and we exclude background earthquakes and magnitude marks. Erlang triggering is a delayed-triggering alternative to the usual power-law ETAS response; the claim does not assert that it is an empirical replacement for the Omori law. Multiplication of time by \(\beta\) does not alter peak counts.

## Proof

For \(\tau=\beta t\), convolution of gamma densities gives the exact, absolutely convergent series
\[
G_m(t)=\beta e^{-\tau}\sum_{n=1}^\infty\frac{q^n\tau^{mn-1}}{(mn-1)!}.
\]
The Laplace transform is \(\widehat G_m(s)=q\beta^m/((s+\beta)^m-q\beta^m)\). For \(m=1\), \(G_1=\beta q e^{-(1-q)\tau}\), proving strict decrease. For \(m=2\), putting \(a=\sqrt q\) yields \(G_2=\beta a e^{-\tau}\sinh(a\tau)\), whose derivative has exactly one positive root \(\tanh(a\tau)=a\), giving one strict maximum.

For \(m=3\), put \(a=q^{1/3}\), \(\theta=(\sqrt3/2)a\tau\), and \(\delta=(1-a)/(1+a)\in(0,1)\). Partial fractions of the Laplace transform yield
\[
G_3(t)=\frac{\beta a}{3}\left[e^{-(1-a)\tau}-e^{-(1+a/2)\tau}(\cos\theta+\sqrt3\sin\theta)\right].
\]
Differentiating this expression shows that its derivative has the same sign as
\[
F(\theta)=\sqrt3\sin\theta-\delta(e^{\sqrt3\theta}-\cos\theta).
\]
The factor \(e^{\sqrt3\theta}-\cos\theta\) is positive for every \(\theta>0\); define \(h(\theta)=\sqrt3\sin\theta/(e^{\sqrt3\theta}-\cos\theta)\). Hence positive-derivative intervals correspond precisely to \(h(\theta)>\delta\). Since \(\delta>0\), only positive-sine half-periods can contribute. For \(0<\theta<\pi\), direct differentiation and the strict inequality below show that \(h\) decreases from \(1\) to \(0\). There is therefore exactly one positive-to-negative derivative crossing (the main peak).

In each later positive-sine interval \(I_j=(2\pi j,(2j+1)\pi)\), \(j\ge1\), one obtains
\[
h'(\theta)=\frac{\sqrt3\,[e^{\sqrt3\theta}(\cos\theta-\sqrt3\sin\theta)-1]}{(e^{\sqrt3\theta}-\cos\theta)^2}.
\]
Writing its bracketed numerator as \(H(\theta)\), the exact identity \(H'(\theta)=-4e^{\sqrt3\theta}\sin\theta<0\) holds on each \(I_j\). Also \(H(2\pi j)>0\), \(H((2j+1)\pi)<0\), so \(h\) has exactly one positive maximum \(d_j\) at \(\theta_j\). In the first interval, \(H(0)=0\) and \(H'<0\), proving the earlier monotonicity. For \(j\ge1\), both endpoints of \(h\) are zero: the inequality \(\delta<d_j\) creates exactly two derivative crossings, a local minimum followed by one new strict maximum. At equality there is only a touching zero with derivative negative on both sides, hence no new extremum; above it there are no crossings.

For each positive-sine angle, \(h(\theta+2\pi)<h(\theta)\). Maximizing each interval implies \(d_1>d_2>\cdots>0\), with \(d_j\to0\) exponentially; since \(\delta=(1-q^{1/3})/(1+q^{1/3})\) strictly decreases as \(q\) increases, the thresholds above are strictly increasing to \(1\). Finally the unique maximizer lies at \(\theta_j=2\pi j+\pi/6+O(e^{-2\pi\sqrt3 j})\), by its defining equation and nonvanishing derivative of \(\cos\theta-\sqrt3\sin\theta\) at \(\pi/6\). Thus \(d_j\sim(\sqrt3/2)e^{-\sqrt3(2\pi j+\pi/6)}\), and expanding \(1-((1-d_j)/(1+d_j))^3\sim6d_j\) gives the asserted asymptotic. These steps cover all \(t>0\) and every \(q\in(0,1)\).

## Verification

Run the supplied standalone `verify_echoes.py` with Python and the packages SymPy and mpmath. It checks the closed-form Erlang renewal series, exact differentiated identities, the first two threshold values, and derivative-sign witnesses on either side of the secondary-peak threshold. These are independent finite checks; the preceding analytic monotonicity argument, not the computation, proves the infinite staircase.

## Relationship to prior work

Seismic ETAS models traditionally use Omori-type power-law kernels (Touati et al., 2011, DOI below), whereas the present precisely specified alternative has an Erlang triggering delay. Duarte, Löcherbach and Ost (arXiv:1610.03300) study Erlang-kernel Hawkes cascades and their stability, not this exact count of strict expected-descendant rate peaks. Cui, Wu and Yin derive Hawkes moments for gamma kernels; their accessible abstract and preview do not establish or exclude this complete threshold classification, so full-text noncoverage is **not** asserted. Likewise, Varsei and Samimi analyze Erlang renewal process moments; their full text was inaccessible, leaving an explicit historical-priority risk. The result is the peak-count and threshold classification, not the known renewal resolvent or general first-moment method.

## Limitations

The threshold \(q_1\) is very close to critical reproduction, so distinguishing the later echoes in finite empirical catalogs may be difficult. The theorem predicts ensemble mean intensity, not peaks in every realized history. External seismicity, magnitudes, observation thresholds, overlapping sources and classical Omori-type kernels are outside the theorem. Source-access limitations leave historical originality provisional; independent validation has not been performed.

## References

1. Touati, Naylor, Main, and Christie, *Masking of earthquake triggering behavior by a high background rate and implications for epidemic-type aftershock sequence inversions* (2011), DOI: 10.1029/2010JB007544; first public online source date checked 2011-03-08.
2. Duarte, Löcherbach, and Ost, *Stability, convergence to equilibrium and simulation of non-linear Hawkes processes with memory kernels given by the sum of Erlang kernels*, arXiv:1610.03300 (first version 2016-10-11).
3. Cui, Wu, and Yin, *Moments for Hawkes Processes with Gamma Decay Kernel Functions*, DOI: 10.1007/s11009-020-09840-8 (published online 2021, journal 2022).
4. Cui, Hawkes, and Yi, *An elementary derivation of moments of Hawkes processes*, DOI: 10.1017/apr.2019.53 (2020).
5. Varsei and Samimi, *Some Results on Renewal Process with Erlang Interarrival Times* (2009), journal abstract accessed; full paper not inspected.
