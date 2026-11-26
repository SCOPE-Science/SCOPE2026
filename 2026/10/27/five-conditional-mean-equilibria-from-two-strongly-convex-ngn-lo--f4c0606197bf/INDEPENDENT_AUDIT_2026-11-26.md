# Independent mathematical audit

## correctness

PASS

Substitution into the positive-floor sampled NGN stepsize gives the asserted odd drift. Its strictly positive denominator leaves x times a quadratic P in x². Two distinct positive roots are equivalent to B<0, C>0, and Δ>0; B<0 and Δ>0 force 16A/(A−1)²<d<2A/(A+1), which is possible exactly above A=5+4√2. Above threshold, at the lower endpoint Δ=0 one has B<0 and C=B²/(4A)>0, so a small positive shift in d gives sufficiency. At equality the strict interval is empty. Independently evaluated the witness exactly via python /workspace/review_evidence/reproduce_1234.py 4: squared nonzero roots 1/15 and 1/5 and multipliers 1145/1156, 73/72, 19/20 at the origin, inner pair and outer pair respectively. The strict multipliers give the asserted local classifications and the outer excess is x²/2=1/10. The threshold is existential over d in this symmetric family. The deterministic conditional-mean iteration is not the stochastic mean across successive steps or a stochastic trajectory.

## originality

PASS

The optimizer and existence of noninterpolation bias are prior; the supported distinct result is the exact five-root existence frontier and the two-loss conditional-mean coexistence witness with classified multipliers.

## value

PASS

The natural uniqueness question for conditional-mean dynamics has a negative answer even with equal curvature, positive losses and two equally weighted samples. The sharp onset and stable suboptimal pair show exactly how uniqueness and local attraction fail, beyond generic mean bias. This is a bounded dynamical statement, not a claim about long-run stochastic behavior.

The dated certificate retains the supplied scientific assessment, sources and limitations.
