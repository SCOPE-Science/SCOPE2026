# Independent mathematical audit

## correctness

PASS

The stationary event-epoch affine recursion Y_n=r(e^(−bL_n)Y_{n−1}+(a/b)(1−e^(−bL_n))) contracts by at most r<1; for b=0, Y=a∑_{j≥1}r^j L_{−j}, a.s. finite by finite mean. Renewal equilibrium time age A has tail P(A>t)=E[(L−t)_+]/μ and is independent of past complete intervals/Y. For b>0, EY=(ra/b)(1−q)/(1−rq), E exp(−bA)=(1−q)/(bμ), giving E M=(a/b)[1−(1−r)(1−q)/(bμ(1−rq))]. Subtracting periodic q0=exp(−bμ) gives positive factor a(1−r)^2(q−q0)/(b²μ(1−rq)(1−rq0)); Jensen strictly minimizes q at deterministic L=μ. At b=0, M=a(A+S) with S=∑r^j L_{−j} independent of A, ES=rμ/(1−r); the equilibrium age A stochastically dominates U∼Uniform(0,μ) because of Jensen on (L−t)_+. Conditional Jensen in S and monotonicity in A then establish the increasing-convex inequality for EVERY nondecreasing convex φ in extended expectation. E A=EL²/(2μ) yields mean a[rμ/(1−r)+EL²/(2μ)] and exact excess a Var(L)/(2μ), including infinite second moment. The two-point L∈{1/2,3/2} has random stationary mass below 1 and above 2 with positive probability, proving no first-order dominance: four short preceding gaps give S<=9/16, age<1/4; four long preceding gaps give S>=23/16 once the >=1/2 lower bound on ALL remaining gaps contributes 1/32, and age>3/4. Independently derived exact mean/variance for three two-point laws; for equal (1/2,3/2), mean=13/8, excess 1/8, stationary variance 53/192. All-renewal claims rest on renewal identities, not simulations.

## originality

PASS

The underlying deposition/partial-leaching physical process and Poisson jump moment equations are established in Suweis et al. and Mau--Feng--Porporato. The main new mathematical comparison quantifies deterministic optimality uniformly over *all iid renewal interval laws with fixed mean* and its sharp zero-uptake increasing-convex order, plus a counterexample forbidding universal fixed-threshold comparison. The inspected primary salinity studies use Poisson/marked Poisson timing or coupled deterministic physicochemistry, and do not supply the all-renewal functional comparison. General renewal age stochastic order is a known ingredient; a more general reset-process convex-order theorem could imply this as a corollary, so novelty is qualified.

## value

PASS

At equal average treatment frequency, the timing distribution controls long-run salt burden: periodic renewal inputs sharply minimize mean for every nonnegative linear uptake coefficient, with an exact distribution-free penalty at zero uptake. The stronger increasing-convex risk comparison and explicit failure of threshold-wise stochastic dominance distinguish usable robust risk advice from an incorrect inference. This is a natural, motivated renewal theorem for a physical partial-reset process, not one arbitrary numerical irrigation schedule. No empirical crop-yield/optimization benefit beyond the model is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
