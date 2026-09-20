# Scientific review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The resolvent of the standard one-dimensional lattice Laplacian is obtained from the decaying root of the second-order recurrence, giving
\[
r_j=\frac{1-q}{1+q}q^{|j|},\qquad s=\frac{q}{(1-q)^2}.
\]
The self-convolution is an elementary three-region geometric sum. Substitution into \(K=2R^2-R\) gives
\[
k_j=q^{|j|}\frac{(1-q)^2}{(1+q)^3}\left(2|j|(1+q)+1-q\right)>0,
\]
with total mass one. Periodization is valid because the kernel is absolutely summable and satisfies the finite circulant resolvent equation. Since \(C\) and \(R\) commute, \(C^kR^m=(CR)^kR^{m-k}\) for \(m\ge k\), proving the stated extension. The two-point Dirichlet matrices at \(s=1\) were multiplied exactly and have negative diagonal entries, so the boundary obstruction is genuine.

The compact verification artifact independently reproduces the infinite-kernel identity to floating-point precision, checks periodization on several cycles and timestep ratios, tests representative \(m\ge k\) powers, and reproduces the exact Dirichlet matrices. These computations support the algebra but are not used in place of the proof.

## Originality

**PASS, to the best of our knowledge, with residual literature risk.** The search covered classical trapezoidal/Crank–Nicolson smoothing, Rannacher damping, positivity-preserving Padé smoothing, exact positivity bounds for Crank–Nicolson heat discretizations, composition-method monotonicity, and recent rational-map positivity work. It also used algebraic searches for the composite \((I-sL)(I+sL)^{-2}\), backward-Euler startup followed by Crank–Nicolson, and periodic/infinite-lattice positivity.

Lindberg (1971), Luskin--Rannacher--Wendland (1982), Rannacher (1984), Khaliq--Wade (2001), Wade et al. (2005, 2007), and Giles--Carter (2006) establish the classical smoothing context. Wade et al. (2005) explicitly introduce smoothing with positivity-preserving Padé schemes, but the accessible statement checked describes a different family based on diagonal Padé main schemes and positivity-preserving damping schemes. Higueras--Roldán (2023) gives exact positivity bounds for unfiltered Crank–Nicolson with homogeneous Dirichlet boundaries. Itkin--Kazbek (2026) gives a recent rational-map positivity analysis in a different Fokker--Planck setting. No checked source supplied the exact positive lattice kernel, its periodization, the \(m\ge k\) factorization consequence, and the Dirichlet failure example together or in an evidently stronger form.

Full theorem-level text was not inspected end-to-end for several historically relevant smoothing papers, particularly Lindberg (1971), Rannacher (1984), Khaliq--Wade (2001), Wade et al. (2005), and Wade et al. (2007). Those are the most plausible sources for hidden equivalent coverage. The originality conclusion therefore remains explicitly provisional.

## Value

**PASS.** The result isolates an exact mechanism behind early-step damping on a canonical heat lattice. Crank–Nicolson itself can have negative entries at large timestep ratios, and the filtered scalar amplification factor is also negative on sufficiently stiff modes; nevertheless the spatial Green kernel after one backward-Euler half-step is strictly positive for every ratio. The closed form explains that phenomenon rather than merely observing it. The \(m\ge k\) corollary gives a simple reusable certificate for early post-startup steps, while the exact Dirichlet counterexample sharply identifies translation invariance as a substantive hypothesis rather than a cosmetic one.

## Scientific limitations

- Standard nearest-neighbor uniform one-dimensional heat lattice only, on \(\mathbb Z\) or periodic cycles.
- The sufficient condition \(m\ge k\) is not claimed necessary.
- No claim that finitely many backward-Euler startup steps protect all later Crank–Nicolson steps.
- Homogeneous Dirichlet boundaries can fail even after two backward-Euler half-steps.
- No extension is proved for arbitrary M-matrices, variable coefficients, nonuniform meshes, finite elements, or higher dimensions.
- No new convergence-order, floating-point, efficiency, or optimal-timestep theorem is claimed.
- The historically relevant sources not inspected end-to-end leave residual originality risk.
