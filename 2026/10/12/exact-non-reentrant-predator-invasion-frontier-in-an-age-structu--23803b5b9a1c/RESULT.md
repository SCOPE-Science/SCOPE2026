# The sharp-maturation age frontier for local predator invasion

## Finding

Consider the unsaturated age-structured predator–prey model of Suarez et al. [1], at the prey-only equilibrium \(\bar x=r/a>0\). Use the exact sharp maturation step at age \(T\), and the numerical section's profiles: baseline fertility is zero before \(T\) and equals \(b_p(e^{-b_{ep}(\tau-T)}+1)\) at ages \(\tau\ge T\); background mortality is \(\mu_B(\tau)=d_pe^{d_{ep}(\tau-L)}\). Let \(h=\mu_Me^{-\rho\bar x}>0\), \(M_B(y)=\int_0^y\mu_B(s)\,ds\), and
\[
Q(T,k)=\int_0^\infty
\left[k\bar x+b_p(e^{-b_{ep}s}+1)(1-e^{-\zeta\bar x})\right]
e^{-h(T+s)-M_B(T+s)}\,ds.
\]
Take \(k,g\ge0\) with the other model parameters positive. The local replacement number in this sharp model is \(R(T,g,k)=e^{-g\bar x T}Q(T,k)\). At each fixed \(g,k\), increasing \(T\) strictly decreases \(R\). If \(Q(0,k)>1\), there is exactly one positive threshold age \(T_c\) for invasion, with
\[
T_c\le \frac{\log Q(0,k)}{h+g\bar x}.
\]
If \(Q(0,k)\le1\), there is no positive age at which invasion is possible. Conversely, for \(T>0\) with \(Q(T,k)>1\) the positive threshold in juvenile predation is \(g_c(T;k)=\log Q(T,k)/(\bar x T)\), strictly decreasing in \(T\). These are local thresholds; a failure to invade does not guarantee global extinction from arbitrary initial conditions.

## Proof

At the prey-only state, the linearized predator transport is autonomous: changes of fertility or mortality with prey abundance are multiplied by the zero equilibrium predator density. The prey block has decay rate \(r\) and is forced by a bounded linear functional of the predator age density. Write \(B_*(\tau)\) and \(\mu_*(\tau)\) for fertility and mortality at \(\bar x\). Then \(B_*\) is bounded, nonnegative and \(\mu_*\ge h\). If \(S(\tau)=\exp(-\int_0^\tau\mu_*)\), the boundary characteristic equation is \(1=\int_0^\infty B_*(\tau)S(\tau)e^{-\lambda\tau}\,d\tau\). At \(R=\int B_*S>1\) its real right side decreases continuously to zero for \(\lambda\ge0\), giving a positive real eigenvalue; \(R=1\) yields the zero eigenvalue.

For completeness, if \(R<1\), choose \(0<\gamma<h\) so \(m_\gamma=\int_0^\infty B_* S e^{\gamma\tau}d\tau<1\), by dominated continuity at zero. Characteristics give the newborn flux as a Volterra convolution of \(B_* S\) with the flux plus the initial-cohort contribution, bounded by \(\|B_*\|_\infty e^{-ht}\|u_0\|_1\). The supremum of the absolute flux weighted by \(e^{\gamma t}\) on any finite time interval is bounded by \(\|B_*\|_\infty\|u_0\|_1/(1-m_\gamma)\), by moving the weighted convolution bound to the left. The age density has an old-cohort norm bounded by \(e^{-ht}\|u_0\|_1\) and a newborn-cohort norm bounded by convolution of the flux with \(S\le e^{-h\tau}\). Thus the age density decays exponentially in \(L^1\); variation of constants gives exponential decay of the forced prey block as well (one can lower the rate to handle equal rates).

In the sharp model the juvenile predation hazard \(g\bar x\) acts precisely before \(T\), and all births occur at or after \(T\). For age \(T+s\), survival is \(e^{-g\bar x T-h(T+s)-M_B(T+s)}\), and adult fertility in the variable \(s\) equals the bracket defining \(Q\). This gives the factorization. The exact sharp model also arises as the limit of the smooth maturation calculation at fixed \(T\): the logistic weights converge almost everywhere to the step indicators, and the weighted fertility is dominated by a constant times \(e^{-h\tau}\).

The integrand of \(Q\) is positive and bounded by a multiple of \(e^{-h(T+s)}\). Dominated convergence gives continuity in \(T\). For \(T_2>T_1\), the nonnegative background mortality gives \(Q(T_2,k)\le e^{-h(T_2-T_1)}Q(T_1,k)\); in particular \(R\) is strictly decreasing and tends to zero. Since \(R(0,g,k)=Q(0,k)\), the intermediate value theorem and the bound with \(T_1=0\) prove the age threshold and its upper bound. For \(T>0\) and \(Q>1\), solving \(R=1\) for \(g\) gives the stated formula; its positive logarithmic numerator decreases while its positive denominator increases. For \(Q\le1\) there is no positive threshold in \(g\).

## Scope and prior work

The age domain here is unbounded; \(L\) is the parameter in the background mortality profile. If one instead imposes a hard maximal age at \(L\), use \(s\in[0,L-T]\) for \(0\le T<L\), and set \(Q=0\) for \(T\ge L\). The age comparison still holds on the active domain by domain inclusion, and the age threshold, when it exists, is below \(L\). No monotone-age conclusion for finite logistic steepness is asserted.

The Euler–Lotka replacement criterion and the smooth model's one-way juvenile-consumption threshold at fixed maturation age are prior results for the same system [2]. The present calculation uses the shifted adult fertility and step maturation to compare different maturation ages and identify the sharp age threshold. The source's numerical phase diagrams do not give this local age frontier. Their attractor classifications need not coincide with a local stability criterion.

## References

1. L. Suarez, M. K. Cameron, W. F. Fagan, D. Levy, “A predator-prey model with age-structured role reversal,” arXiv:2502.19748; *Journal of Mathematical Biology* 92 (2026), 73, DOI 10.1007/s00285-026-02402-5, §§2.2 and 6.1.
2. “Juvenile consumption creates a unique predator-invasion cutoff,” Resultary, 2026-10-04, `e1bfc3bf3626`.
