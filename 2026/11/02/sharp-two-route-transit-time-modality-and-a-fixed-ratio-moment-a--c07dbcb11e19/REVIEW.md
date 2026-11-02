# Self-review

## Correctness — PASS

For an exponential branch in parallel with \(k\) equal-rate serial reservoirs, the full normalized density is explicitly stated, including the support \(t\ge0\), stage integer \(k\ge1\), positive rates and strictly interior route weights. Differentiating yields one elementary sign-determining function \(\Phi_{k,R}\), and the strict monotonicity of its logarithmic derivative gives exactly one hump for \(k\ge3\). The separate \(k=2\) boundary calculation gives the sharp extra rate-contrast threshold \(R=2\), and \(k=1\) follows directly. Equality produces nonpeak shoulders rather than extra strict maxima. Both rational triples have exactly \(\mathbb ET=1\), \(\mathbb ET^2=493/242\), ratio \(a/b=3\), and lie on rigorously opposite sides of the \(k=3,R=3\) critical weight. Exact algebra in `proof_check.py` and 800 sampled derivative checks replayed successfully. Finite checks corroborate, but do not replace, the complete derivative proof.

## Originality — PASS within inspected scope; priority conditional

Došlá (2009), full text pp. 280–290, gives general criteria for mixtures and explicit gamma results for *equal shapes* (Proposition 6) or *equal rates* with shapes both greater than one (Proposition 7). It explicitly states that general different-shape, different-rate gamma mixtures are not handled in that paper. Our claimed specialization uses shape one versus integer shape \(k\), with unrestricted positive and possibly unequal rates; it obtains a complete explicit peak-count and boundary-mode threshold and one exact fixed-rate-ratio moment alias. The general Došlá/Kemperman criterion is acknowledged as applicable in principle, rather than dismissed. Fang (2001) defines the broad hyper-Erlang family, without the inspected material stating the threshold. Roa-García–Weiler (2010) and Heidbüchel et al. (2012) motivate tracer transit-time distributions, not this parameter-uniform modality theorem. Johnson–Taaffe (1989) study common-order mixtures and matching moments; the related 1990 article on density-function shapes was discovered but not fully accessible. Searches of relevant mathematical literature and published database summaries did not uncover the exact two-route theorem, but a previously known specialized phase-type result could still dominate it. This is unresolved independent historical-priority risk; search failure is not a uniqueness proof.

## Value — PASS

A one-well-mixed-route plus a serial-reservoir-route model is a natural minimal representation for fast and delayed tracer travel in a heterogeneous catchment. The classification tells when an initially high tracer release is followed by a genuinely separate delayed peak, for every stage number and positive rate contrast. The exact same-mean, same-variance, same-rate-ratio pair shows that two commonly reported summary statistics cannot determine the number of tracer peaks even when the rate contrast is fixed. These are interpretable structural constraints on idealized tracer signals, not a claim of field-identifiable networks or of improved parameter fitting.

## Closest sources and remaining risks

- Došlá, *Kybernetika* 45 (2009), pp. 279–292: full relevant results and discussion read; its general criterion may yield alternate reductions and is not treated as absent prior art.
- Fang, *Wireless Networks* 7 (2001): hyper-Erlang density and moment machinery predates this work; no priority claimed for the mixture model itself.
- Roa-García and Weiler, *Hydrol. Earth Syst. Sci.* 14 (2010): tracer transit and hydrologic response must not be conflated.
- Heidbüchel et al., *Water Resour. Res.* 48 (2012): exponential/gamma transit functions and mass-weighted superpositions are prior work; no formula for the stated modality boundary was located in the inspected article.
- Johnson and Taaffe (1989, 1990): phase-type moment matching and density-shape results are highly pertinent. Only summaries/metadata of the 1990 work were available; full text was unavailable after limited retrieval efforts. The possibility of direct or stronger coverage is a residual priority risk.

Self-review: passed. Independent audit: not yet performed.
