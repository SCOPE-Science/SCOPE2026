# Independent audit — 2026-09-28

Record: `2026/09/11/035`  
Audited tree: `44e146fae95fa77c379e5643e0264d8211e719bc`  
Disposition: **passed**

## Correctness

I independently checked the arithmetic inputs: `10069` is prime, `10069 ≡ 7 (mod 9)`, `30207=3·10069`, `(12·10069)^2=14599405584`, and the Mordell coefficient is `-432·30207^2=-394183950768`. The cubic-residue computation gives `3^((10069-1)/3) ≡ 5363 (mod 10069)`, hence the cubic symbol used by the record is nontrivial.

The open full-text preprint of Das–Jha proves, in the `ℓ ≡ 7 (mod 9)` case, that under the nontrivial cubic-symbol hypothesis the relevant 3-isogeny Selmer group over `Q(ζ_3)` has dimension at most 2; parity forces dimension 1, and their exact sequence then gives `S_3(E_{-432(3ℓ)^2}/Q)=0`, hence Mordell–Weil rank 0. This is the exact logical route used for `ℓ=10069`. The committed helper script is useful for the finite arithmetic, but its theorem-level booleans are not treated as an independent proof.

## Originality

Targeted searches found the general family theorems and nearby numerical examples but no prior table or publication entry for `ℓ=10069` / `D=30207`. The novelty is therefore only the explicit certified instance, not a new Selmer theorem.

## Scientific value

The record is a modest but reproducible database-style exact instance in a root-number `+1` family, with a concrete Selmer/rank certificate. Its value should be read at that finite-instance level.

## Sources and limitations

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/11/035
- https://www.researchgate.net/publication/394396073_On_certain_root_number_1_cases_of_the_cube_sum_problem
- https://doi.org/10.1016/j.jpaa.2025.108145
- https://arxiv.org/abs/2207.12487

Oxford institutional retrieval was attempted only after arXiv/OA checks; it stopped at a human-verification gate, so I do not claim to have read material available only behind that gate. The OA preprint supplied the decisive proof passage.
