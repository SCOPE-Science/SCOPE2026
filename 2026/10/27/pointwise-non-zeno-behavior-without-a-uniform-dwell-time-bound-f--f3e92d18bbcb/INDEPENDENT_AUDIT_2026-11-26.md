# Independent mathematical audit

## correctness

PASS

On a held interval the mean is (1−τ)a_k and the mean-zero component is the free heat solution. At a purported positive finite accumulation time T, the shrinking gaps are eventually less than one, so the sampled means are bounded. A nonzero mean-zero component has strictly positive norm at T by injectivity, and its derivative is bounded on [T/2,T] by 2||h_0||/(eT). Consequently the state increment is at most C times the interval length, while at a finite event continuity and the strict-trigger infimum imply it is at least ε||h(T)||. This contradicts gaps tending to zero. Strong continuity gives a positive first event time for nonzero initial data; zero has no events; pure nonzero mean repeats gaps ε/(1+ε), before the mean can hit zero. On a nonconstant eigenmode the feedback vanishes and the trigger ratio is exp(n²π²τ)−1, so each gap equals log(1+ε)/(n²π²). This rules out a lower bound uniform in the initial state, not a bound along any particular orbit. Checked RESULT.md:17–47 and VERIFICATION.md:19 analytically, without finite-dimensional truncation.

## originality

PASS

Credit Wakaiki–Sano for precisely the same eigenmode calculation and the resulting zero infimum for first-event time. The surviving distinct contribution, already distinguished and credited in the frozen record, is non-accumulation for every fixed L² initial state under the same full-state trigger, including arbitrary mixtures of Neumann modes. The source's finite-dimensional and feedback-error theorems do not supply it.

## value

PASS

Settles the missing trajectory-level question in a specific published example often used to show a failure of uniform event-time analysis. It gives a rigorous separation between arbitrarily fast sampling across initial states and impossible finite-time accumulation on any one orbit. The trajectory-wise lower norm and finite-time smoothing argument is needed precisely where the published high-frequency witness provides no such guarantee.

The dated certificate retains the supplied scientific assessment, sources and limitations.
