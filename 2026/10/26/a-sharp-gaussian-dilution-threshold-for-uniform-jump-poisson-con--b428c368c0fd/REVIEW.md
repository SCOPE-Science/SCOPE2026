# Independent mathematical audit

## correctness

PASS

Integrating e^(tu) against the quadratic integrated jump tail gives 2K(t)/(Vt^2)=1+wtH(t), with H(0)=E[J^3]/(3E[J^2]). The candidate scale function phi=wH/(1+wtH) is strictly below 1/t at positive t, so any t with phi>c is within the tested pole domain, establishing the exact unconstrained supremum. Its derivative has sign H'/H^2-w. Under the stated log-concavity, the tilted density e^(tu)h(u)/H(t) has increasing hazard (integrate its decreasing density ratio f(s+v)/f(s)), making its survival submultiplicative. The integrated second-moment bound E_t[U^2]<2(E_t[U])^2 is strict because r,s below the finite endpoint can have r+s above it on a set of positive measure. Thus (H'/H^2)'<0, and H'/H^2 tends to zero by the finite-support bound on H'/H and exponential growth of H. This proves uniqueness globally, including the strictly decreasing positive-t optimizer at equality and the true-variance normalization. Independent piecewise integration and rational Taylor arithmetic (python /workspace/checks/5.py with SymPy; output /workspace/checks/5.txt) confirm the integrated tail, matching through two derivatives, curvature, w*=868/1125, sigma^2/lambda cutoff 257/372, and g'(0)=-9716/84375. Inverting the stationarity equation then gives the cited linear t coefficient and quadratic excess w* H(0)^2/(-2g'(0)). Clarification: the >=1 conditional in the general Finding is vacuous under its log-concavity hypothesis. Indeed h(0)=1 and log-concavity imply h(r+s)<=h(r)h(s), strictly on a set of positive measure by bounded support, so H'(0)=integral integral h(r+s) dr ds < H(0)^2. The remark that the raw moment threshold expression can exceed one applies only outside the log-concave class (e.g. masses 999/1000 and 1/1000 at jumps 1 and 10); it does not affect the asserted classification or uniform constants. Submitted code was inspected, not run.

## originality

PASS

Pass for the global shape-based single crossing and the continuous uniform jump classification with its onset, not for the variational transform, a local/interior dichotomy in general, fixed-jump Gaussian dilution, or the use of increasing hazard for log-concave densities. The same-day unequal-jump phase surface has material overlap at its Gaussian endpoint, where its positive jump has constant size one, but its hypotheses do not yield the variable-amplitude uniform law or the general kernel criterion. No publication order between the same-day records is asserted.

## value

PASS

This is a sharp true-variance concentration parameter for noisy marked counts. The kernel condition turns an implicit unbounded optimization into a strictly single-crossing equation across an entire positive-jump class. The bounded continuous uniform law is a useful exact benchmark distinct from fixed-size jumps; its quadratic excess measures when and how much the local third-cumulant scale ceases to suffice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
