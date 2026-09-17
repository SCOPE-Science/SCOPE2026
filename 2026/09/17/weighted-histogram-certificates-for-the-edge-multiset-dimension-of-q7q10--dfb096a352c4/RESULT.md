# Weighted-histogram certificates for the edge multiset dimension of Q7–Q10

> **Review status: same-model review.** Correctness, originality and value were assessed by the same-model review, not an independent reviewer. Originality is claimed only to the best of our knowledge; consult `REVIEW.md` for limitations. Publication is not peer review or a guarantee of priority.

## Claim

For the hypercubes `Q_d`, the source run reports

- `edim_m(Q_7) >= 9`,
- `edim_m(Q_8) >= 10`,
- `edim_m(Q_9) >= 11`,
- `edim_m(Q_10) >= 12`.

Equivalently, `edim_m(Q_d)>=d+2` for `d in {7,8,9,10}` only. No all-`d` theorem is claimed.

Combined with Allikvere's explicit certificates, this yields the source-run brackets

- `9 <= edim_m(Q_7) <= 63`,
- `10 <= edim_m(Q_8) <= 115`,
- `11 <= edim_m(Q_9) <= 246`,
- `12 <= edim_m(Q_10) <= 492`.

## General certificate principle

For an edge `e` and landmark set `S` of size `m`, let

`H_e^S=(H_e^S(0),...,H_e^S(d-1))`

be the edge-distance histogram. There are

`E_d=d*2^(d-1)`

edges. For every edge, shell capacity is

`c_r=2*C(d-1,r)`,

so any actual histogram is among the integer tuples with `sum h_r=m` and `0<=h_r<=c_r`.

For a fixed landmark `s`, exactly `d*C(d-1,r)` edges are at edge-distance `r`, hence

`sum_e H_e^S(r)=d*m*C(d-1,r)`.

For any nonnegative integer weight vector `w`, define

`W_w(h)=sum_r w_r h_r`.

The total score of all actual edge histograms is forced to be

`T(d,m,w)=d*m*sum_r w_r*C(d-1,r)`.  (1)

Let `L(d,m,w)` be the sum of the `E_d` smallest scores among distinct admissible histograms. If fewer than `E_d` admissible histograms exist, resolving is impossible by counting; otherwise any resolving set must satisfy `T>=L`. Therefore `L>T` certifies nonexistence.

## Explicit certificates

Weights:

- `d=7`: `(2,1,0,0,0,1,2)`
- `d=8`: `(4,2,1,0,0,1,2,4)`
- `d=9`: `(3,2,1,0,0,0,1,2,3)`
- `d=10`: `(3,2,1,0,0,0,0,1,2,3)`

For `Q_7`, `E=448`. For `m=1,...,5`, there are at most 406 admissible histograms. For the remaining sizes:

- `m=6`: `L=1336`, `T=672`
- `m=7`: `L=1098`, `T=784`
- `m=8`: `L=909`, `T=896`

Thus `edim_m(Q_7)>=9`.

For `Q_8`, `E=1024`. For `m=1,...,5`, at most 720 admissible histograms exist. Then:

- `m=6`: `L=7675`, `T=3744`
- `m=7`: `L=6686`, `T=4368`
- `m=8`: `L=6134`, `T=4992`
- `m=9`: `L=5770`, `T=5616`

Thus `edim_m(Q_8)>=10`.

For `Q_9`, `E=2304`. For `m=1,...,5`, at most 1197 admissible histograms exist. Then:

- `m=6`: `L=15239`, `T=5076`
- `m=7`: `L=12206`, `T=5922`
- `m=8`: `L=10517`, `T=6768`
- `m=9`: `L=9426`, `T=7614`
- `m=10`: `L=8476`, `T=8460`

Thus `edim_m(Q_9)>=11`.

For `Q_10`, `E=5120`. For `m=1,...,6`, at most 4566 admissible histograms exist. Then:

- `m=7`: `L=25540`, `T=7980`
- `m=8`: `L=20556`, `T=9120`
- `m=9`: `L=17194`, `T=10260`
- `m=10`: `L=14566`, `T=11400`
- `m=11`: `L=12732`, `T=12540`

Thus `edim_m(Q_10)>=12`.

## Reproducibility

The source report reports two independent exact implementations: direct recursive enumeration of admissible histograms and dynamic programming of the score distribution. It states that both agree for every displayed certificate and that all arithmetic was exact. It also reproduces the preceding SCOPE `Q_6>=8` bound as a consistency check, but explicitly does not count that as the fresh contribution of this run.

The source report says its locally generated supporting files could not be attached because those files were not included in the supplied package. Those unavailable files are not fabricated or republished here.

## Prior work and scope

The closest primary source is Jaan Allikvere, *The edge multiset dimension of hypercubes*, arXiv:2608.09983v1, which establishes the finite/infinite transition and gives explicit resolving sets for `Q_6` through `Q_10` but leaves exact minimum sizes open. The source run also checked Ikhlaq--Ismail--Siddiqui--Nadeem (2023), Farhan--Klavžar--Kuziak--Yero (arXiv:2607.10311), and Albejani--Lin--Ryan--Sugeng (arXiv:2607.08128).

## Limitations

Exact values remain unknown; the certificates are dimension-specific; no general `d+2` theorem is claimed. A simple extension to `d=11` did not certify `m=d+1`, so the run stopped rather than extrapolating. Originality remains qualified by indexing latency and unpublished work. No independent validation is claimed.
