# Independent mathematical audit

## correctness

PASS

Square completion gives Γ_k=A²P_{k+1}²/(R+P_{k+1}); the scalar recursions reproduce a=ε²/[16(1+ε²)(5+4ε²)], b=1/[16(1+ε²)], c=ε/3 and ℓ=ε³ in the frozen notation. Under the source's exact reception and prediction/reset convention the squared errors are fixed by the realized binary schedule; neither the selected auction schedule nor the minimizing schedule signals initial signs. The source's current-decision bid sums over the whole remaining horizon, hence the first comparison is a+b−ℓ>c−ℓ>0, and both next bids are −ℓ. All nine feasible schedules reduce to the five listed costs by deletion of wasteful packets. The differences between each alternative and a+2ℓ are c−a−ℓ, b−ℓ, c−ℓ and (b−ℓ)+(c−ℓ), all strictly positive on 0<ε≤1/10. The ratio is therefore (c+ℓ)/(a+2ℓ)∼80/(3ε). In particular the exact result concerns the objective after removing the same schedule-independent constant on both sides. Both plants have A=1/2; the source requires finite moments, not nondegenerate Gaussian inputs, and admits zero process noise.

## originality

PASS

The primary paper defines the auction and exact benchmark, and reports numerical performance, but explicitly leaves analytic suboptimality bounds to future work. The inspected single-agent antecedents do not define the same shared-capacity competition. No covering statement of the stable scalar horizon-two separation was identified in the bounded source and index comparisons.

## value

PASS

The paper introduced a practical low-complexity policy and motivated an analytic performance comparison. This example identifies why its horizon-summed bids can misallocate a scarce current slot, even for stable scalar plants with only two stages. The strict unbounded separation holds for the actual objective passed to the schedule optimizer, so it rules out a specific guarantee rather than reporting a large finite example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
