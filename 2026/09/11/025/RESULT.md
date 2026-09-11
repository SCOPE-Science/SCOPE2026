# Refutation of the nominated quaternion Azumaya class on the diagonal quartic X: x^4+4y^4-9z^4-36w^4=0

## Context

The admitted target proposed a transcendental Brauer–Manin Hasse-principle
failure on the smooth diagonal quartic K3 surface
X: x^4+4y^4-9z^4-36w^4=0 via the quaternion class A=(theta,-1) with
theta=(x^2+2y^2)/(z^2+2w^2), asserting A in Br(X)[2] transcendental with
constant local-invariant sum 1/2. Audit-plan Step 2 requires verifying
Azumaya membership (residue check along divisors). This result resolves the
TARGET by disproving that clause.

## Definitions

- X subset P^3_Q: x^4+4y^4-9z^4-36w^4=0.
- theta=(x^2+2y^2)/(z^2+2w^2) in Q(X)^x.
- A=(theta,-1) in Br(Q(X)), quaternion (2-torsion) class.
- K=Q(a), a^2=-2; X_K=X x_Q K.
- L=V(x-a*y) subset P^3_K; D^+=X_K cap L.
- For a prime divisor D in residue characteristic !=2 and constant c,
  the tame residue of (f,c) is [c^{v_D(f)}] in k(D)^x/squares.

## Result

Let X, theta, A, K, D^+ be as above. Then:

1. D^+ is a prime divisor on the smooth surface X_K (isomorphic to the
   smooth plane curve 8y^4-9z^4-36w^4=0), met transversely everywhere,
   with v_{D^+}(theta)=1.
2. The tame residue is d_{D^+}(A)=[-1] != 0 in k(D^+)^x/squares.
3. Hence A is ramified along D^+, so A not in Br(X_K) and a fortiori
   A not in Br(X).
4. In particular the target conjunction asserting A in Br(X)[2]
   transcendental with constant sum 1/2 is false as stated.

## Proof / evidence

1. Smoothness: grad F_X=(4x^3,16y^3,-36z^3,-144w^3) vanishes in A^4 only
   at the origin in characteristic 0, so X is smooth (K3), hence integral;
   theta is nonzero in Q(X)^x.
2. Over K, x^2+2y^2=(x-ay)(x+ay) with a^4=4. On L, D^+ is
   8y^4-9z^4-36w^4=0, smooth (gradient (32y^3,-36z^3,-144w^3) only at
   origin), hence integral and geometrically irreducible, a prime divisor
   with K algebraically closed in k(D^+). Gradients of F_X and x-ay are
   dependent only at z=w=0, forcing y=0 then x=0, invalid in P^3; so the
   intersection is transverse everywhere and x-ay is a uniformizer,
   v_{D^+}(x-ay)=1.
3. Point P=[a:1:zeta:0] with zeta^4=8/9 in Kbar lies on D^+ since
   a^4+4-9 zeta^4=4+4-8=0, with x+ay=2a != 0 and z^2+2w^2=zeta^2 != 0.
   Hence neither other factor vanishes identically, and
   v_{D^+}(theta)=1+0-0=1.
4. Tame symbol gives residue [-1]. If (u+av)^2=-1 with u,v in Q then
   uv=0 and u^2-2v^2=-1, i.e. p^2+r^2=2q^2 with pq=0, impossible:
   q=0 gives p^2+r^2=0 forcing p=r=0; p=0 gives r^2=2q^2 contradicting
   2-adic parity (v2 of LHS even, RHS odd). So -1 is not a square in K
   (T^2+1 irreducible), and since K is algebraically closed in k(D^+),
   [-1] != 0.
5. By purity Br(X_K)=intersection ker(d_D), A not in Br(X_K); by
   restriction Br(X)->Br(X_K), A not in Br(X). Deductive proof, not
   experimental evidence.

## Limitations

- Refutes only the nominated representative (theta,-1) with
  theta=(x^2+2y^2)/(z^2+2w^2).
- No conclusion about X(Q), X(A_Q), local solubility, the
  elliptic-fibration rank, Hilbert-symbol values of any other class, or
  any repaired neighboring symbol.

## Reproducibility

`python3 output/artifacts/verify.py` prints `VERIFY_OK` (stdlib only).
It checks the a^4+4-9(8/9)=0 identity, nonvanishing of other factors at P,
transversality case analysis, smoothness case analyses, and the 2-adic
parity obstruction for -1 in K^{x2}.

## References

- E. Ieronymou, Diagonal quartic surfaces and transcendental elements of
  the Brauer group, arXiv:0911.1268.
- E. Ieronymou, A. Skorobogatov, Odd order Brauer-Manin obstruction on
  diagonal quartic surfaces, doi:10.1016/j.aim.2014.11.004.
- T. Santens, Diagonal quartic surfaces with a Brauer-Manin obstruction,
  doi:10.1112/s0010437x22007916.
- M. Bright, The Brauer-Manin obstruction on a general diagonal quartic
  surface, doi:10.4064/aa147-3-8.
- T. Preu, Example of a transcendental 3-torsion Brauer-Manin obstruction
  on a diagonal quartic surface, doi:10.1017/cbo9781139525350.013.
- D. Gvirtz, A. Skorobogatov, Cohomology and the Brauer groups of diagonal
  surfaces, doi:10.1215/00127094-2021-0029.
