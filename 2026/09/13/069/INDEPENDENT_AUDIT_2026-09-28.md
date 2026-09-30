# Independent audit — 2026-09-29
- Source: `2026/09/13/069`
- Assigned/current tree SHA: `8bfcd63f3c3f375227a6399f84da697bfac2f61c`
- Disposition: **repaired**

## Three-axis assessment

### Correctness

**PASSED** — Independent symbolic computation reproduces det(Df_t(p_2)-I)=s^2+2s-2, the root s*=sqrt(3)-1, the factorization -(lambda-1)(lambda^2-4lambda-1), and d mu/dt=-2*pi*sqrt(3). A nonhyperbolic fixed point at t* indeed excludes Anosov and the definition of t_c gives t_c<=t*. The committed artifact agrees with these calculations.

### Originality

**PASSED** — The exact matrix/shear family, threshold value, spectrum and eigenvalue slope are family-specific calculations not supplied by general structural-stability or almost-Anosov results. The repair removes priority language and states only the exact family-specific result; no broader theorem used in the comparison yields this numeric obstruction without the submitted computation.

### Scientific value

**PASSED** — The exact neutral fixed point is a concrete obstruction that bounds the admissible Anosov interval and identifies the local loss-of-hyperbolicity mechanism. Its value is narrow and explicitly does not extend to equality t_c=t* or to a theorem on uniform mixing.

## Independent checks

- rederived the fixed point p_2 and derivative matrix
- symbolically expanded the determinant and characteristic polynomial
- computed exact left/right eigenvectors and the simple-eigenvalue derivative
- verified the committed artifact is artifacts/bifurc.py and that the old RESULT/METADATA pointed to the wrong output/artifacts path
- confirmed main has no changes under this record since the inventory commit

## Limitations

- Does not prove t_c=t* or Anosov persistence up to t*.
- Does not prove critical slowing or non-uniform mixing.
- Open-access sources were sufficient; Oxford Download was not needed.

## Citations

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/13/069
- https://doi.org/10.1112/jlms/jdt073
- https://arxiv.org/abs/1707.09221
