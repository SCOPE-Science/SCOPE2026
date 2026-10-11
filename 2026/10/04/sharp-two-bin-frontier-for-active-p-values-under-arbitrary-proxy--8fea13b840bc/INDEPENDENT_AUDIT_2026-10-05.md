# Independent mathematical audit

## correctness

PASS

At testing level \(s\), an adversarial proxy chooses the bin giving the larger activation probability among bins whose scaled threshold contains the realized \(P\). This produces the decreasing envelope \(g_s(p)=h_2\) for \(p\le s/b_2\), \(h_1\) for \(s/b_2<p\le s/b_1\), and zero afterward, with thresholds capped at one. Since every valid null p-value stochastically dominates Uniform\([0,1]\), the worst expectation is the uniform integral \(W(s)=h_1\min(1,s/b_1)+(h_2-h_1)\min(1,s/b_2)\). Piecewise inspection shows \(W(s)\le s\) for every \(s\) exactly when the displayed coefficient is at most one. Necessity is attained by a uniform \(P\) and a deterministic proxy-bin selection realizing the envelope for sufficiently small \(s\). A fresh randomized grid replay found exact agreement between the criterion and the envelope test in 5000 parameter draws; this is supplementary to the analytic proof.

## originality

PASS

The most relevant active-p-value paper explicitly gives sufficient decomposition conditions under arbitrary dependence and notes that they are not necessary; its general-dependence construction does not state an exact frontier for this two-bin multiplier family. Xu et al. use a different randomized active-p-value map. Resultary and targeted exact searches found no equivalent necessary-and-sufficient two-bin calibration condition.

## value

PASS

The result gives an exact robust-calibration frontier under arbitrary dependence in the smallest nontrivial proxy discretization, including a necessity construction and examples beyond the source's sufficient class. Such a finite-bin characterization is directly useful for designing valid active tests rather than merely checking one parameter choice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
