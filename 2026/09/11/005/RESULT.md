# No resonance in the A=10 target window for the square double barrier

## Context

The admitted target claimed that for the symmetric square double barrier
`V_A = A*(1_{[-2,-1]} + 1_{[1,2]})`, `A >= 10`, with `H_A = -d^2/dx^2 + V_A`
on `L^2(R)`, every `A >= 10` supports a shape resonance `k_1(A)` with
`|Re k_1 - e_1| <= 1/10` and `0 < -Im k_1 <= exp(-sqrt(A-3))`, where
`e_1 = pi/2` is the Dirichlet ground frequency of the cavity `(-1,1)`.
A universal claim is falsified by one counterexample. This record certifies
the `A = 10` counterexample: the claimed rectangle is empty of resonances.

## Definitions

- `e_1 = pi/2`, `b = exp(-sqrt(7)) ~= 0.0709520267`.
- `R = [e_1 - 1/10, e_1 + 1/10] x [-b, 0]`, a closed rectangle.
- For `A = 10`, on barrier intervals use `kap = sqrt(10 - k^2)` (principal
  branch), `A_1 = [[cosh kap, sinh kap / kap],[kap sinh kap, cosh kap]]`;
  on the cavity `B = [[cos 2k, sin 2k / k],[-k sin 2k, cos 2k]]`;
  `U = A_1 B A_1` propagates `(u,u')^t` from `-2` to `2`.
- Resonance function `S(k) = i k tr U + k^2 U_{01} - U_{10}`.
- `T_{22}` is the `(2,2)` entry of the scattering transfer matrix;
  `T_{22} = 0` is the resonance condition. Exact identity:
  `T_{22}(k) = e^{4ik} S(k) / (2ik)`.

## Result

For `V_{10} = 10*(1_{[-2,-1]} + 1_{[1,2]})`, `H_{10}` has **no** resonance
`k` with `|Re k - pi/2| <= 1/10` and `0 < -Im k <= exp(-sqrt(7))`.
Equivalently, `S(k) != 0` (hence `T_{22}(k) != 0`) for every `k` in `R`.
Therefore the `for every A >= 10` uniform target claim is false.

## Proof / evidence

1. `S` is holomorphic on a neighbourhood of `R`: on `R`,
   `|k| >= 1.4`, `|kap| >= 2.6`, `|10-k^2| >= 7.1`, so all denominators
   and the square root stay away from singularities (asserted and checked
   inside the enclosure).
2. `output/artifacts/verify_nozero.py` evaluates `S` in midpoint-radius
   complex ball arithmetic over a finite subdivision of `R`, checking
   `|S(mid)| > radius` per cell. It terminates with 2 cells and minimum
   exclusion margin 8.18. Replay: `python3 output/artifacts/verify_nozero.py`
   prints `VERIFY_OK` in a fraction of a second (stdlib only).
3. The factor `e^{4ik}/(2ik)` never vanishes on `R` (`|k| >= 1.47`), so
   zeros of `T_{22}` coincide with zeros of `S` there.
4. Independent auditor confirmation: `|S| >= 400` on a `41x41` grid and on
   the rectangle boundary; rectangle winding number `0`; Newton iteration
   locates the nearest true resonance at `k* ~= 1.18519977 - 0.00102523i`
   (residual `~3e-14`), with `Re k* - e_1 ~= -0.3856`, distance `~0.286`
   left of `R`. The width bound holds (`0.00103 < b ~= 0.0709`); the
   location bound fails. Reported windings on `|k-e_1| = 0.1, 0.25` are `0`
   at `A = 10, 16, 20, 25`, and Newton Re-shifts follow `~1/sqrt(A)`,
   reaching `0.1` only around `A ~= 300`: the obstruction is structural.

## Limitations

- Disproof covers the `A = 10` instance only (sufficient to falsify the
  universal claim); the large-`A` regime (`A ~= 300+`) is not certified here.
- The certificate covers exactly the rectangle `R`.
- The resonance location `k*` is a residual-certified computation
  (residual `~3e-14`), not an enclosure.
- No statement is made about any hidden fallback or repaired window.

## Reproducibility

- `python3 output/artifacts/verify_nozero.py` -> `VERIFY_OK` (2 cells,
  min margin `8.179124`, identity cross-check included).

## References

- F. M. Fernandez, Resonances for symmetric two-barrier potentials,
  arXiv:1107.4092 (smooth double barrier, numerical only, different potential).
- Y. Latushkin, A. Pogan, Resonances for the 1D Schrodinger operator with
  the matrix-valued complex square-well potential, arXiv:2509.00235
  (single connected well, explicitly non-novel, different object).
