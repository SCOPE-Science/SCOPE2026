# Independent mathematical audit

## correctness

PASS

Pass applies to the complete corrected /workspace/repairs/1/RESULT.md, not the frozen noncommutation statement at RESULT.md line 23. At fixed n, coupling the chord clock as E/λ makes it eventually arrive after all ordinary edges almost surely as λ decreases to zero. Its expected contribution then tends to the probability both endpoints are vacant in the ordinary terminal matching. Distinct fixed truncation neighborhoods are independent for large n by separation along both arcs, and the factorial descending-path bound removes the truncation. Each limiting vacancy probability is h(1)²=e⁻², so the two iterated limits through positive rates both equal e⁻⁴. Setting λ=0 denotes deleting the chord and gives zero, not a different iterated limit. The repaired fixed-positive-rate theorem also checks independently: the half-line message h(x)=e⁻ˣ comes from h′=−h in uniform ordinary-edge time; the bridge message uses its two independent arms and acceptance uses all four. For the successive ordinary messages, the deviations are iterated integrals with alternating sign and a uniform factorial majorant. Summing their recurrence gives S(x)=e⁻ˣ∫₀ˣk(y)dy where k is the bridge challenge probability in the cavity experiment. The four-arm aggregate after reversing the integrals contains −∫φλ(y)e⁻⁴ʸdy, cancelling the bridge acceptance term and leaving the stated defect. Coupling the cycles with and without the chord gives influence only along strictly decreasing earlier-neighbor paths in the line graph; the bound 4^r/r! times at most four edges per distance is summable and also justifies local convergence. The Beta(1,λ) quantile coupling and strictly increasing g(x)=e⁻²ˣ(2x−1) give continuity, strict decrease and the endpoint limits, with λ=1 integration giving −e⁻⁴. Expansion after y=1−x gives the convergent series in the corrected proof; an independent 40-term evaluation with bisection gives λ*≈0.42594602097919343, consistent with the printed precision. The original verify.py was inspected, not run; its floating-point finite recursion and quadrature are supplementary and do not cover the iterated-limit proof.

## originality

PASS

For the corrected finding, the supported distinct result is the exact order-one signed terminal matching defect of one asymptotically long chord with a variable arrival rate, and the unique sign reversal. Line-graph locality and generic nonmonotonicity were known; the corrected weak-rate argument distinguishes a late surviving attempt from removal of an edge, without relying on a spurious noncommutation as a contribution.

## value

PASS

After correcting the weak-rate interpretation, the natural one-defect problem still has a useful exact answer: the macroscopic density masks an order-one change in expected total matching size, and the smallest augmentation studied here can help or harm purely by changing its timing. The explicit sign threshold and unit-rate deficit distinguish the actual response from generic locality or nonmonotonicity. The corrected analysis also explains why a slow chord may increase the terminal count without suggesting that the two positive-rate iterated limits differ.

The dated certificate retains the supplied scientific assessment, sources and limitations.
