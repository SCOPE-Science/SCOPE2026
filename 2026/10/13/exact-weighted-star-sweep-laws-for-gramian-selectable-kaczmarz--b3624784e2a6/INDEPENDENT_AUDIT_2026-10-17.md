# Independent mathematical audit

## correctness

PASS

The star Gramian follows because distinct leaf rows e_i are orthogonal and each meets scaled center sqrt(w/m)1. Under exact Algorithm 3 update, selecting a leaf removes it and re-enables center; selecting center resets all leaves. From post-center S=all leaves, a successful episode selects all m leaves before center with p_G=prod_{r=1}^{m-1}r/(r+w). Renewal and episode-length tail probabilities give E T_G=C(m+w,m-1)+C(m+w-1,m-1)-1. IID ordinary RK draws center probability w/(m+w); success p_R=prod_{r=1}^m r/(r+w), with E center count 1/p_R-1; Wald yields E T_R=(m+w)/w(1/p_R-1). Gamma-ratio asymptotics yield ratio (w+1)/w for fixed w>0. A full leaf sweep without intervening center sets all leaf coordinates exactly because leaves are orthogonal; it is only a sufficient certificate, NOT the first actual solution hitting. Independent rational state recurrences agreed for 40 (m,w) pairs m2..9 and weights 1/4,2/3,1,3/2,4.

## originality

PASS

The IID reset-coupon gamma baseline is already published in Resultary and must NOT be claimed novel. The distinct GSSRK star without replacement leaves has a state-dependent center hazard absent from that baseline or the Kaczmarz primary paper. Only the exact structural selectable-selector certificate, its w dependence and differential asymptotic remain original best of knowledge.

## value

PASS

Quantifies a meaningful structural bottleneck and sampling-rule speed effect for a natural analyzable Gramian star, including the ability to change row-selection probabilities by rescaling an algebraically redundant equation. Explicitly separates an exact sufficient sweep certificate from actual first hitting. The mathematical conclusion can guide algorithm comparison but does not assert general practical speed gains.

The dated certificate retains the supplied scientific assessment, sources and limitations.
