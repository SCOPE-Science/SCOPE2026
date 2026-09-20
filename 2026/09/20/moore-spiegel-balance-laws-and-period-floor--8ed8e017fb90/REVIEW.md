# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness — PASS

The two polynomial balances were independently expanded symbolically; all residuals
vanish exactly. The invariant-measure identities follow by integrating Lie
derivatives against a compactly supported invariant probability measure.

The \(T<0\) bounded-orbit argument was checked against the fact that the origin
need not be linearly attracting: the theorem is intentionally conditional on
boundedness and does not claim global attraction of all initial conditions.
Monotonicity of \(\mathcal F\), boundedness, and uniform continuity imply decay
of \(x,y,z\).

At \(T=0\), the first balance only directly controls \(y\), so the proof also
uses the second balance to show \(z\in L^2\), and the exact first integral
\(K=z+y-R(x-x^3/3)\) to obtain convergence of \(x\) when \(R\ne0\). The
\(R=0\) case was checked separately from the explicit linear equations.

For the period bound, nonconstancy makes \(\int x^2>0\), so the balance forces
\(T>0\). Averaging the jerk equation proves zero mean of \(x\). Sharp Wirtinger
then gives \(P\ge2\pi/\sqrt T\). The equality case was tested by substituting
the first harmonic back into the full nonlinear jerk equation; the remaining
term is \(R(x^2-1)x'\), excluding equality for \(R\ne0\). For \(R=0\), the
linear factorization confirms that equality is actually attained.

For the support threshold, the second balance makes the \(y^2d\mu\)-weighted
mean of \(x^2\) strictly larger than \(1-T/R\) for every nontrivial compact
invariant measure when \(R>T>0\). The possibility \(\int z^2=0\) was checked:
compact invariance inside \(z=0\) forces \(y=0\) and then \(x=0\) for \(T>0\).

## Originality — PASS

The result was compared with the established Moore--Spiegel literature by
object, parameter regime, periodic-orbit claims, global dynamics, and generalized
jerk formulations.

- Moore--Spiegel (1966) introduced the model and studied periodic/aperiodic
  behavior.
- Baker--Moore--Spiegel (1971) is the most important historical risk because it
  studied periodic solutions analytically and numerically, including stability
  and averaging. Its full text was not inspected; bibliographic records and
  later descriptions were inspected. This leaves residual uncertainty about
  whether an equivalent period inequality or one of the auxiliary balances was
  recorded there.
- Marzec--Spiegel (1980) relates the oscillator to strange attractors and the
  earlier averaging analysis; its accessible abstract does not state the exact
  identities or global period floor.
- Balmforth--Craster (1997) was inspected in full. It develops bifurcation
  structure, synchronization, and periodic-orbit expansions and supplies
  numerical periods, but the inspected theorem/equation/table material did not
  provide the invariant-measure balances, \(T\le0\) compact-recurrence
  classification, damping-threshold support theorem, or parameter-only strict
  period floor.
- Letellier--Malasoma (2014) studies topology and parity for generalized
  Moore--Spiegel equations. Its full text was not inspected; the abstract was.
  It is a secondary coverage risk.
- Igra (2024) proves strong topological information about the Moore--Spiegel
  flow and its periodic trajectories. The available theorem/abstract material
  concerns reduction to solid-torus dynamics and knot type rather than these
  integral balances or period inequality.
- A September 2026 control paper concerns local feedback stabilization at a
  standard chaotic parameter set, not the global recurrence statements here.

Searches using exact and synonymous combinations of "Moore-Spiegel", invariant
measure, moment/balance law, mean square, bounded solutions, period lower bound,
and global stability did not reveal a matching theorem. Repository searches for
the Moore--Spiegel object also found no prior SCOPE result.

Originality is therefore assessed PASS to the best of our knowledge, with the
1971 and 2014 inaccessible full texts explicitly retained as coverage risks.

## Value — PASS

The result supplies one common exact mechanism for periodic, quasiperiodic and
chaotic compact recurrence rather than describing a single numerically observed
attractor. It gives:

- a universal RMS relation between velocity and displacement;
- a second exact moment constraint involving acceleration and nonlinear damping;
- a complete exclusion of bounded non-equilibrium recurrence for \(T\le0\);
- an explicit amplitude excursion that every nontrivial recurrent state must
  make when the damping changes sign;
- a sharp, parameter-only period floor, with a complete equality
  characterization.

These constraints are directly checkable against numerical or experimental
Moore--Spiegel trajectories and complement the literature's bifurcation,
periodic-orbit, topological, and control analyses.

## Scientific limitations

The measure results require compact support. The convergence result assumes
forward boundedness and does not provide a global absorbing set. The amplitude
threshold requires \(R>T>0\). The strict period inequality does not prove
existence of cycles. Historical coverage remains uncertain where full text was
not inspected, especially Baker--Moore--Spiegel (1971).
