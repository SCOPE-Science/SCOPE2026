# Independent mathematical and primary comparison

Primary arXiv:2609.20053v1 Eq.10, Section3 parameterization and the complete Section4.2 sensitivity derivation were read. The published fixed-coarse-load choice is confirmed; it is a valid surrogate, not generally one fixed physical load's pullback.

Independent differentiation gives
\[
J'=2(F_c')^Tq-q^TK_c'q.
\]
The residual identity additionally assumes exact Galerkin Kc=T^TKT; direct DEIM stiffness interpolation is not automatically that identity. The general load derivative formula does not need this extra equality. For the rank-one example at pi/4, the exact, stiffness and load contributions are 4/25, -6/25 and 2/5. The full-space rotation gives zero from -3/2+3/2. A scalar coordinate gauge shifts the stiffness contribution by -2cJ and the load term by its opposite. No implementation or benchmark failure is claimed. General chain-rule/Pulay ideas are prior framework; source-specific correction is the originality boundary.
