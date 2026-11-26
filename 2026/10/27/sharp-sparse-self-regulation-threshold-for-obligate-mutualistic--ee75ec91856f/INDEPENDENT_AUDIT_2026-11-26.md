# Independent mathematical audit

## correctness

PASS

At a positive equilibrium let P=diag(z). J=PK is similar to P^{1/2}KP^{1/2} and hence its inertia equals that of the symmetric per-capita derivative K. The unregulated principal block has eigenvalue −D, D=d+b−bk; thus strict stability requires k<1+d/b (equivalently k≤ceil(d/b)). At equality, the coupling to the nonempty regulated block gives a positive Rayleigh quotient by perturbing the unregulated all-ones vector slightly in the positive regulated direction. At B≤0 the summed balance is impossible. For B,D>0 choose common h on m>0 species. The unregulated equation gives Dy=bmx−a; substitution gives hx²−Cx+E=0 with C=B(d+b)/D, E=a(d+b)/D (direct for k=0). Both roots for 0<h<C²/(4E) exceed a/B, so y>0 since bm=B+D. On group-constant coordinates, the Schur complement of −D in K is C−2hx; all within-group eigenvalues are negative. For k=0 the collective eigenvalue is directly B−2hx. The signs at the two roots are opposite, proving the full-state stability counts and a simple zero at the fold. To verify the actual saddle-node, write v as 1 on regulated coordinates and bm/D on unregulated coordinates (omit the latter when k=0); at the fold Kv=0. With left vector P^{-1}v, the projections of the parameter derivative and second state derivative along v are −m x² and −2hm, respectively, both nonzero. The fold is established for the stated common-h family; no inference about general unequal coefficients is needed. In fact, for the common-h choice group equality at a positive fixed point also follows from strict monotonicity of (d+b)z_i+h_i z_i²=bΣz_j−a. The rational example gives D=1/2 and h_fold=45/16 and both balances check. The frozen determinant script is a finite check of the construction, not an infinite proof or a separate necessity certificate; it was inspected, not executed.

## originality

PASS

The distinctive result is the exact minimum support for one fixed-sign self-only term per regulated species in the symmetric complete model, and the associated explicit branch/fold and full-state signs. Pairwise impossibility, unconstrained higher-order rescue, Schur complement arguments, and mutualism folds are not new. The closest inspected results do not establish the support minimum under these restrictions.

## value

PASS

The exact support minimum answers how much of an already-fixed unstable mutualism network must receive a restricted negative self-term, rather than simply showing that enough nonlinear terms can create a stable state. The obstruction identifies an unregulated cooperative block that strength elsewhere cannot overcome, including at the integer equality boundary, and the matching family identifies both sides of the usable parameter window. This is a model-specific local-stability result, not a claim of ecological feasibility, biomass bounds or global attraction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
