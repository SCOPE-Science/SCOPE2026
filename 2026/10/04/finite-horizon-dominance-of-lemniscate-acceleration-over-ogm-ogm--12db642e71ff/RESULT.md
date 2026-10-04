# Finite-horizon dominance of lemniscate acceleration over OGM--OGM-G chaining
## Finding

Let \(f\) be an \(L\)-smooth convex function with a minimizer \(x_\star\), and let
\[
R=\|x_0-x_\star\|.
\]
For an even horizon \(N\ge2\), the recent lemniscate-acceleration theorem gives the exact certified bound
\[
G_{\rm lem}(N)
=
\frac{L^2R^2}{\Omega_N^2},
\]
where \(\Omega_N\) is the unique scalar defined by the paper's recurrence. The same paper records the standard certificate obtained by running OGM for \(N/2\) steps and OGM-G for \(N/2\) steps:
\[
G_{\rm chain}(N)
=
\frac{64L^2R^2}{(N+2)^4}.
\]

The exact lemniscate certificate is strictly smaller at every finite even horizon:
\[
G_{\rm lem}(N)<G_{\rm chain}(N)
\qquad
\text{for every even }N\ge2.
\]
Equivalently,
\[
\Omega_N>\frac{(N+2)^2}{8}.
\]
Hence the advantage of lemniscate acceleration over this standard two-phase baseline is not merely an improvement of the leading asymptotic constant: there is no small-horizon crossover among the even horizons for which the chained guarantee is stated.

Define the certified-guarantee ratio
\[
Q_N
=
\frac{G_{\rm lem}(N)}{G_{\rm chain}(N)}
=
\frac{(N+2)^4}{64\Omega_N^2}.
\]
Then \(Q_N<1\) for every even \(N\ge2\). Using the source asymptotic law
\[
\frac{\Omega_N}{(N+1)^2}\longrightarrow\frac1{\varpi^2},
\]
one also has
\[
Q_N\longrightarrow\frac{\varpi^4}{64}\approx0.738565.
\]

## Assumptions and scope

The comparison is between two published worst-case *guarantees*, not a claim that one algorithm's realized gradient norm is pointwise smaller on every objective. Both bounds use the same smooth-convex class, the same initial-distance quantity \(R\), and the same count \(N\) of gradient steps. The chained OGM--OGM-G expression is stated for even \(N\), so the new all-horizon statement is restricted to even horizons.

The coefficient \(\Omega_N\) is the unique admissible scalar for the recurrence
\[
\Omega_N(\rho_k-\rho_{k+1})^2
=
\rho_k(1-\rho_{k+1}^2),
\qquad
1=\rho_0>\rho_1>\cdots>\rho_{N+1}=0.
\]

## Proof

The desired guarantee inequality is equivalent to
\[
\frac1{\Omega_N^2}<\frac{64}{(N+2)^4},
\]
which, since all quantities are positive, is equivalent to
\[
\Omega_N>\frac{(N+2)^2}{8}.
\]
Write
\[
T_N=\frac{(N+2)^2}{8}.
\]

For the large-horizon tail, the source proves
\[
\Omega_N>\frac{(N+1)^2}{\varpi^2},
\]
where
\[
\varpi=2\int_0^1\frac{dx}{\sqrt{1-x^4}}.
\]
We first establish the elementary certified bound
\[
\varpi<\frac{27}{10}.
\]
Indeed, with
\[
S(x)=1+x+x^2+x^3,
\]
one has
\[
\frac{\varpi}{2}
=
\int_0^1\frac{dx}{\sqrt{(1-x)S(x)}}.
\]
Partition \([0,1]\) at \(j/16\), \(j=0,\ldots,16\). On the cell \([a,b]\), monotonicity of \(S\) gives
\[
\int_a^b\frac{dx}{\sqrt{(1-x)S(x)}}
\le
\frac{2(\sqrt{1-a}-\sqrt{1-b})}{\sqrt{S(a)}}.
\]
Summing the sixteen bounds and multiplying by two gives an explicit radical upper sum. The bundled exact-rational enclosure of those radicals proves
\[
\varpi<2.685342<2.7.
\]
Consequently,
\[
\Omega_N
>
\frac{100(N+1)^2}{729}.
\]
For \(N=21+m\) with \(m\ge0\), direct expansion gives
\[
800(N+1)^2-729(N+2)^2
=
71m^2+1666m+1559>0.
\]
Therefore
\[
\frac{100(N+1)^2}{729}
>
\frac{(N+2)^2}{8}
=
T_N
\]
for every \(N\ge21\), in particular for every even \(N\ge22\).

It remains to treat
\[
N\in\{2,4,6,8,10,12,14,16,18,20\}.
\]
The source gives an exact shooting test. For fixed \(\Omega\ge1\), set \(\Phi_0(\Omega)=1\) and, while \(\Omega\Phi_k(\Omega)\ge1\), define
\[
\Phi_{k+1}(\Omega)
=
\frac{
\Omega\Phi_k(\Omega)
-
\sqrt{
\Phi_k(\Omega)^2
+
\Omega\Phi_k(\Omega)(1-\Phi_k(\Omega)^2)
}
}{
\Omega+\Phi_k(\Omega)
}.
\]
Its bisection theorem states that if some \(k\le N\) satisfies
\[
\Phi_k(\Omega)<\frac1\Omega,
\]
then \(\Omega<\Omega_N\).

The bundled exact-rational interval checker evaluates this criterion at \(\Omega=T_N\). It encloses every square root between rational lower and upper bounds, propagates an interval for every \(\Phi_k(T_N)\), verifies that all preceding steps remain in the admissible domain, and certifies a strict crossing before or at index \(N\) for every one of the ten remaining even horizons. Therefore
\[
T_N<\Omega_N
\]
for all ten base horizons as well.

Combining the finite certificates with the analytic tail proves the finite-horizon dominance for every even \(N\ge2\).

Finally, the source proves
\[
\frac{\Omega_N}{(N+1)^2}\longrightarrow\frac1{\varpi^2}.
\]
Substitution into
\[
Q_N=\frac{(N+2)^4}{64\Omega_N^2}
\]
yields
\[
Q_N\longrightarrow\frac{\varpi^4}{64}.
\]

## Verification

`artifacts/verify_finite_horizon.py` uses only exact integer and rational arithmetic. It supplies outward rational enclosures for every square root by integer square-root bounds at fixed decimal scale. It verifies the sixteen-cell certificate \(\varpi<27/10\), proves the exact positive tail polynomial, and applies the source shooting criterion to all ten exceptional even horizons.

The checker reports `VERIFY_OK`. The finite computation is exhaustive only for the ten explicitly listed base horizons; the infinite tail is handled by the analytic inequality above, not by enumeration.

## Relationship to prior work

Kim, Ryu, and Das Gupta derive the exact lemniscate certificate \(L^2R^2/\Omega_N^2\), prove the lower bound \(\Omega_N>(N+1)^2/\varpi^2\), give an exact bisection/shooting characterization of \(\Omega_N\), and show the asymptotic law \(\Omega_N/(N+1)^2\to1/\varpi^2\). In their comparison paragraph they state the even-horizon OGM--OGM-G chained guarantee \(64L^2R^2/(N+2)^4\) and compare only the leading asymptotic constants, reporting an improvement of about \(1.35\).

Kim and Fessler's OGM-G work develops the optimized gradient-norm method and proves its gradient guarantees under the relevant smooth-convex initial conditions. The later lemniscate paper combines standard OGM and OGM-G guarantees into the baseline used here.

The new statement resolves the finite-horizon comparison left open by an asymptotic-constant discussion: the exact lemniscate certificate beats that chained certificate at every admissible even horizon, including the small horizons where the asymptotic constant alone cannot decide the comparison.

Targeted literature and published-result searches using finite-horizon, crossover, exact \(\Omega_N\), lemniscate acceleration, OGM, and OGM-G aliases did not locate this all-even-horizon statement.

## Limitations

The result compares certified upper bounds, not realized objective-by-objective trajectories and not independently optimized lower bounds for the two algorithms.

The chained baseline is the standard OGM--OGM-G guarantee quoted by the recent source. Other restart, regularization, or horizon-dependent combinations are outside the claim.

The finite exceptional cases rely on exact rational interval certificates derived from the source's proved shooting criterion. The checker does not attempt to recompute the source convergence theorem itself.

## References

1. H. Kim, E. K. Ryu, S. Das Gupta, *A Domain-Specific Harness for End-to-End Automation of Optimization Research*, arXiv:2608.07407v1, 2026.
2. D. Kim, J. A. Fessler, *Optimizing the Efficiency of First-Order Methods for Decreasing the Gradient of Smooth Convex Functions*, Journal of Optimization Theory and Applications 188, 192--219, 2021. DOI: 10.1007/s10957-020-01770-2; arXiv:1803.06600.
3. D. Kim, J. A. Fessler, *Optimized First-Order Methods for Smooth Convex Minimization*, Mathematical Programming 159, 81--107, 2016. DOI: 10.1007/s10107-015-0949-3; arXiv:1406.5468.
