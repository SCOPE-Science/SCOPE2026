# No U-polarized K3^[2] fourfold carries two holomorphic Lagrangian fibrations along its two isotropic rays

## Context

Let $X$ be a projective irreducible holomorphic symplectic fourfold of
$K3^{[2]}$-type. Its second cohomology carries the Beauville–Bogomolov–Fujiki
form $q$ of signature $(3,20)$ on the lattice
$L = U^3 \oplus E_8(-1)^2 \oplus \langle -2\rangle$ (rank 23).
The admitted target asks about the Neron–Severi lattice $NS(X) \cong U$,
the hyperbolic plane spanned by primitive isotropic classes $f_1,f_2$ with
$q(f_i)=0$ and $(f_1,f_2)=1$: does every such $X$ admit two pairwise
non-isomorphic holomorphic Lagrangian fibrations over $\mathbf{P}^2$ with
fiber classes along $f_1$ and $f_2$, distinct up to $Aut(X)$?

## Definitions

- $U$: rank-2 lattice with Gram matrix $[[0,1],[1,0]]$; for
  $x = af_1+bf_2$, $q(x)=2ab$ and
  $(af_1+bf_2,cf_1+df_2)=ad+bc$.
- MBM class (K3^[2]-type, Mongardi): primitive $q=-2$, or $q=-10$ with
  divisibility 2. Each defines a wall $\delta^\perp$ avoided by the
  K\"ahler cone (Amerik–Verbitsky).
- Holomorphic Lagrangian fibration of a K3^[2] fourfold: holomorphic
  $\pi:X\to\mathbf{P}^2$ (Matsushita/Hwang) with Lagrangian fibers;
  $F=\pi^*\mathcal{O}(1)$ is nef with $q(F)=0$ by the Fujiki relation.
- $j_0:U\hookrightarrow L$: isometric embedding as the first $U$-summand;
  $F_1=e_1$, $F_2=f_1$; $\delta=F_1-F_2$; $T=j_0(U)^\perp$.

## Result

The universal two-fibration claim is FALSE. No projective
$K3^{[2]}$-type fourfold $X$ with $NS(X)\cong U$ spanned by the two
isotropic rays admits holomorphic Lagrangian fibrations over
$\mathbf{P}^2$ along both $f_1$ and $f_2$, let alone two distinct up to
$Aut(X)$. On every such $X$ at most one of the two isotropic rays is nef,
hence at most one can support a holomorphic fibration. An explicit
$U$-polarized $X$ (first-summand embedding, very general period in
$\Omega_T$, K\"ahler class $2F_1+F_2$) with Mukai flop datum
$R_\delta$ witnesses at most one holomorphic fibration along $\{f_1,f_2\}$,
disproving the universal assertion.

## Proof / evidence

1. Lattice wall (exact computation): $\delta=f_1-f_2$ satisfies
   $q(\delta)=-2$, is primitive in $L$, and has divisibility
   $div_L(\delta)=1$ since $(\delta,F_1)=-1$, $(\delta,F_2)=+1$ generate
   $\mathbf{Z}$. Hence $\delta$ is MBM and $\delta^\perp$ is a wall of the
   K\"ahler chamber decomposition. Reflection
   $R_\delta(x)=x+(x,\delta)\delta$ is an integral involutive isometry of
   $L$ swapping $F_1\leftrightarrow F_2$, fixing $F_1+F_2$ and every vector
   of $T$ pointwise. Verified in `check_lattice.py` and
   `check_embedding.py` with exact integer arithmetic.
2. Unique separating wall: in $U$, $q=-2$ classes are exactly
   $\pm\delta$, and every $q=-10$ class ($ab=-5$) has $\gcd(|a|,|b|)=1$,
   so no $q=-10$, div-2 MBM class exists in $U$. Thus $\delta^\perp$ is
   the unique wall meeting $NS(X)_\mathbf{R}$. Since
   $(f_1,\delta)=-1<0<+1=(f_2,\delta)$ while
   $(f_1+f_2,\delta)=0$ with $q(f_1+f_2)=2>0$, the wall passes through the
   interior ray $\mathbf{R}_{>0}(f_1+f_2)$ of the positive cone and the two
   isotropic rays lie strictly on opposite sides. The nef cone, the closure
   of the K\"ahler cone, satisfies $(x,\delta)\ge 0$ on one chamber, so it
   contains at most one isotropic ray; $Aut(X)$ preserves the nef cone, so
   no automorphism exchanges the rays.
3. Fibration classes: if $\pi:X\to\mathbf{P}^2$ is holomorphic Lagrangian
   with $F=\pi^*\mathcal{O}(1)$, then $F$ is nef and $q(F)=0$ by Fujiki
   ($F^3=0$). In $U$, $q(af_1+bf_2)=2ab=0$ iff $a=0$ or $b=0$, so every
   holomorphic fibration fiber class is a positive multiple of $f_1$ or
   $f_2$. Combined with step 2, at most one ray carries a holomorphic
   fibration, and the two putative fibrations cannot coexist or be
   $Aut(X)$-translates.
4. Existence: $T\cong U^2\oplus E_8(-1)^2\oplus\langle-2\rangle$ has period
   domain $\Omega_T\ne\emptyset$; a very general period gives Picard lattice
   exactly $j_0(U)$. With $\kappa=2F_1+F_2$ ($q=4$, $(\kappa,\delta)=-1$),
   period-map surjectivity and Torelli supply a marked $(X,\eta)$ with
   $\eta^{-1}(\kappa)$ K\"ahler, hence projective with $NS(X)=U$. On this
   $X$ the $f_1$-ray is nef while the $f_2$-ray is not, so at most one
   holomorphic fibration occurs. $R_\delta$ fixes $H^{2,0}\subset T$ and is
   a Hodge monodromy giving the birational Mukai flop $X\dashrightarrow X'$
   to the adjacent chamber, exchanging the rays; it moves the K\"ahler cone
   so is not induced by $Aut(X)$.

## Limitations

The argument cites standard cone and Torelli theorems (Mongardi MBM
classification, Amerik–Verbitsky K\"ahler description, Markman monodromy and
Torelli, period-map surjectivity) rather than reproving them; machine
checks cover only the lattice and reflection inputs. The exhibited $X$ is
established by a general existence argument with explicit lattice data, not
by equations of a concrete projective model. No claim is made about
rational (non-holomorphic) fibrations on the flopped model.

## Reproducibility

Run `python3 check_lattice.py` and `python3 check_embedding.py` in
`output/artifacts/`; both terminate with ALL CHECKS PASSED and emit
`lattice_check.json` and `embedding.json` recording $q(\delta)=-2$,
divisibility 1, separation pairings, and reflection properties.

## References

- Mongardi: MBM classification for K3^[n]-type.
- Amerik–Verbitsky: K\"ahler cone via MBM/prime-exceptional walls.
- Markman: monodromy, reflections, Torelli for hyperk\"ahler manifolds.
- Bayer–Macr\`i: MMP/wall-crossing, birational Lagrangian fibrations.
- Matsushita/Hwang: fibration structure and base $\mathbf{P}^2$.
- Huybrechts; Verbitsky/Markman; Demailly–P\u00e4un: surjectivity and
  K\"ahler-chamber realization.
