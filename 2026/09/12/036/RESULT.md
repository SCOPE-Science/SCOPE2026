# Single-square obstruction for the cone over the split nodal cubic over F7

## Context

The admitted target asked for the group K_{-1}(S) of the affine cone S = Spec F7[X,Y,Z]/(Y^2Z-X^3-X^2Z) over the split nodal cubic via a single smooth cdh blow-up long exact sequence at the origin, with branches (A) K_{-1}(S)=Z from a vertex loop or (B) a strictly larger value from a surviving cocycle. Both branches presupposed that Bl_0(S) with exceptional divisor the nodal cubic C forms a smooth cdh blow-up square.

## Definitions

F = Y^2Z-X^3-X^2Z over F7. S = Spec F7[X,Y,Z]/(F). C = V(F) subset P^2_{F7}. pi: Bl_0(S) -> S is the blow-up at the origin with exceptional divisor E. KH denotes Weibel homotopy K-theory. NK denotes Bass nil-K fiber of K -> KH.

## Result

Theorem (single-square obstruction). (i) Sing(S) = V(X,Y), the z-axis, not an isolated vertex. (ii) Bl_0(S) is singular along the proper transform of the z-axis: in the Z-chart the strict transform is the cylinder B^2-A^3-A^2=0 singular along the line A=B=0, while the X-chart U^2V-V-1=0 and Y-chart C(1-A^2)-A^3=0 are smooth. (iii) Hence (Bl_0(S),E) -> (S,0) is not a smooth cdh blow-up square, so K_{-1}(S) cannot be read off from one smooth square; correct descent needs the normalization/conductor square with K_0 of the non-reduced conductor or a further blow-up along V(x,y) plus characteristic-7 Frobenius analysis. (iv) KH_{-1}(S)=KH_{-1}(F7)=0 by cone A1-contractibility, so any K_{-1} class is Bass/NK type. Partial ledger: H^1(C,O(m))=0 for m>=1 (checked m=1..4 with evaluation rank 2) and H^1(C,O)=F7.

## Proof and evidence

By hand Jacobian: grad F = (-3X^2-2XZ, 2YZ, Y^2-X^2). If Y != 0 then Z=0, then F=-X^3=0 gives X=0 hence Y^2=0, contradiction; so Y=0, then -X^2=0 gives X=0 with F automatic. Thus Sing(S)=V(X,Y). Brute force over A^3(F7) reproduces exactly 7 singular points all with X=Y=0 (output/artifacts/geom.py). Strict transforms: X-chart (U=Y/X,V=Z/X): G_X=U^2V-V-1=0, grad (2UV,U^2-1); on U^2=1, G_X=-1 != 0, smooth. Y-chart (A=X/Y,C1=Z/Y): G_Y=C1(1-A^2)-A^3=0, grad (-2AC1-3A^2,1-A^2); on A^2=1, G_Y=-A^3 != 0, smooth. Z-chart (A=X/Z,B=Y/Z,C=Z): G_Z=B^2-A^3-A^2=0 free C, grad (-3A^2-2A,2B,0) vanishing along A=B=0 for all C; other A-roots of 3A+2=0 do not combine with B=0 on the surface over F7 in a new component, so the singular line persists. Hence Bl_0(S) singular. E is the nodal cubic: C=0 section in Z-chart, X=0 section in X-chart. Split node: tangent cone Y^2-X^2=(Y-X)(Y+X), slopes +-1; normalization [U:V] -> [(U^2-V^2)V:(U^2-V^2)U:V^3], i.e. t -> (t^2-1,t(t^2-1),1), verified on C for all t in F7 with node fiber t=+-1={1,6} (geom.py). H^1 ledger: O(m) pulls back to O(3m) on P1; two split node preimages impose independent conditions for degree >=1; evaluation matrix rank 2 for m=1..4, rank 1 only at m=0 (output/artifacts/ledger.py). KH: H((x,y,z),t)=(tx,ty,tz) is an A1-homotopy from id_S to the vertex; KH is A1-invariant so KH(S) ~= KH(F7) and KH_{-1}(S)=0 since F7 is regular.

## Limitations

The exact group K_{-1}(S) remains open: the normalization/conductor square with K_0 of the non-reduced conductor and char-7 Frobenius on H^1_cdh(S,O) were prescribed but not completed. The vanishing ledger covers nodal curve twists, not full H^1_cdh(S,O). No external CAS or literature conductor computation was available.

## Reproducibility

Stdlib-only Python 3 scripts output/artifacts/geom.py and output/artifacts/ledger.py re-run deterministically; reported outputs are: 7 singular affine points all X=Y=0; param lands on curve True; fiber [1,6]; m=0 evalrank 1 => H1=F7; m=1..4 evalrank 2 => H1=0.

## References

G. Cortinas, C. Haese meyer, M. Schlichting, C. Weibel, Cyclic homology, cdh-cohomology and negative K-theory, Ann. Math. 167 (2008). G. Cortinas et al., K-theory of cones of smooth varieties, J. Alg. Geom. 22 (2013). T. Yusof, K_{-1} and higher reduced K-groups of cones of smooth plane curves, Bull. Malays. Math. Sci. Soc. 45 (2022) -- smooth-base case only, hence boundary of this singular-base obstruction. C. Weibel, Negative K-theory of normal surfaces, Duke 108 (2001); Negative K-theory of varieties with isolated singularities, JPAA 34 (1984). M. Kerz, F. Strunk, G. Tamme, Algebraic K-theory and descent for blow-ups, Invent. Math. 211 (2018).
