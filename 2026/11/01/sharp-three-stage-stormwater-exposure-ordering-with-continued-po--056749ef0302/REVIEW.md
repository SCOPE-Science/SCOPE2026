# Scientific review

## Correctness — PASS

The theorem concerns exactly six permutations of three pairwise-distinct rates \(a>b>c>0\), common stage length \(h>0\), and positive initial stock and source. Conservation gives \(P+M=m+st\). The stage transfer formula and its time integral are derived directly from the linear differential equation, so the claimed exposure is an exact expression for the stated quantity. Using \(1-u_r=rz_r\), the order-dependent supply term becomes \(s z_a z_b z_c\) times the middle rate. Strict cumulative-hazard comparisons eliminate two maximum and two minimum candidates. The remaining gaps have exact signs governed by \(m/s=z_a\) and \(m/s=z_c\), including every tie. Two-stage source invariance proves minimality. The standalone `verify.py` independently integrates each stage and tests 22,058 assertions; samples are not used as an infinite proof. Source mass, units, positivity, initial conditions, and tie cases were checked.

## Originality — PASS within inspected evidence, provisional

The empirical exponential runoff wash-off basis is established in Sartor and Boyd (1972). Vaze and Chiew (2003; first public date 19 June) experimentally investigate rainfall energy and runoff intensity, not permutation-optimal accumulated-pool time exposure. Soonthornnonda et al. (2008) derive an exponential within-event pollutant wash-off model with initial dry-period loading; they do not optimize arbitrary orders of three equal-duration coefficient stages under simultaneous fresh supply. Chen and Adams (2006) formulate joint buildup/wash-off and probability-distribution stormwater control, but do not state the present deterministic three-stage order classification. Generic scalar variation of constants and pairwise hazard sorting are acknowledged and insufficient by themselves to state both threshold switches and middle-rate invariance. Searches for equivalent rate sequencing and accumulation exposure found no direct implication. A general linear-system sequencing theorem may precede this characterization; earlier inaccessible hydrological work is a residual priority risk, not evidence of noncoverage.

## Value — PASS

Stormwater studies distinguish pollutant availability, fresh deposition, wash-off intensity, and time distribution of runoff. For an unflushed receiving pool, time-integrated accumulated load gives extra weight to early export, unlike final total load. The result is a motivated complete exact classification: source-to-initial-load ratio can reverse both extremal orderings, with two sharp physically dimensioned thresholds, ties, no dependence of switch positions on the intermediate rate, and a rigorous two-stage impossibility. The result is a reusable structural benchmark for interpreting simple event-shape idealizations, not a practical recommendation to reorder natural rainfall.

## Closest literature and limitations

- Sartor and Boyd (1972), *Water Pollution Aspects of Street Surface Contaminants*, EPA-R2-72-081: original exponential wash-off phenomenology.
- Vaze and Chiew (2003), DOI 10.1029/2002WR001786: full open experimental paper and motivation for deposition/removal balance; not an ordering theorem.
- Chen and Adams (2006), DOI 10.1029/2005WR004540: full analytical stormwater buildup/wash-off and control framework; different observables and stochastic event-distribution analysis.
- Soonthornnonda et al. (2008), DOI 10.1016/j.scitotenv.2008.04.036: publicly available author manuscript inspected through model, data analysis and conclusions; separate dry-time buildup and event wash-off, not simultaneous supply and three-stage objective.
- Barbé, Cruise and Mo (1996), DOI 10.1111/j.1752-1688.1996.tb04049.x: accessible abstract only; full article was unavailable. It concerns long-period pollutant buildup and power-law event wash-off; unseen portions remain a priority risk.

Single-stock linear dynamics, no receiving-pool decay, equal durations, and constant continuing supply are essential. No new empirical claim or fully verified historical priority is asserted.

Self-review: passed. Independent audit: not yet performed.
