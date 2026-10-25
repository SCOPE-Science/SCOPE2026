# Exact shadowing reduction and a branching obstruction for finite-symmetry multivalued dynamics

## Finding

Let a finite group \(G\) act isometrically on a compact metric space \((X,d)\), and let a continuous \(G\)-equivariant map \(f:X\to X\) induce \(T:X/G\to X/G\). For the set-valued map \(F(x)=Gf(x)\), ordinary shadowing and periodic shadowing are each equivalent, with identical admissible \((\delta,\varepsilon)\) pairs, to the corresponding property of \(T\) in the quotient metric. Moreover, \(F^n(x)=\pi^{-1}(T^n\pi x)\), so its period-dividing-\(n\) point counts are weighted by orbit-fibre size. Positive expansivity of \(F\) implies that of \(T\); the converse holds for free actions, but fails for an explicit two-sheet Cantor wedge whose quotient is the one-sided binary full shift. In that nonfree example both maps have shadowing and periodic shadowing, yet only the quotient is positively expansive, and the set-valued periodic-point zeta equals \((1-z)/(1-2z)^2\).

## Assumptions and scope

All orbits and pseudo-orbits are forward infinite. A multivalued orbit is a sequence \((z_i)_{i\ge0}\) with \(z_{i+1}\in F(z_i)\). A \(\delta\)-pseudo-orbit is a sequence satisfying \(d(z_{i+1},F(z_i))<\delta\). A periodic pseudo-orbit has some period \(n\ge1\), and periodic shadowing asks for an actual periodic multivalued orbit at uniform distance below \(\varepsilon\); the actual orbit's period need not equal \(n\). Ordinary shadowing is the analogous property without periodicity. These are the set-valued definitions used in the cited literature.

The quotient \(Y=X/G\) has metric \(\bar d([x],[y])=\min_{g\in G}d(x,gy)\), and \(\pi:X\to Y\) denotes the quotient. No freeness or faithfulness of the action is assumed unless explicitly stated. Positive expansivity means that some \(\alpha>0\) forces two orbits with distinct initial points to be more than \(\alpha\) apart at some nonnegative time. For the point-count zeta, define \(P_n(F)=|\{x\in X:x\in F^n(x)\}|\) when finite and \(\zeta_F^{\rm pt}(z)=\exp(\sum_{n\ge1}P_n(F)z^n/n)\) as a formal power series. This counts periodic **points**, not distinct multivalued orbit realizations.

## Proof

**1. Quotient dynamics and the exact pseudo-orbit identity.** Since the action is finite and isometric, \(\bar d\) is a compact quotient metric. Equivariance makes \(T([x])=[f(x)]\) well defined and continuous. Every fibre \(\pi^{-1}([u])\) is exactly a \(G\)-orbit, so
\[
F(x)=\pi^{-1}(T(\pi x)),\qquad
 d(y,F(x))=\bar d(\pi y,T(\pi x)). \tag{1}
\]
Equation (1) is exact, including at nonfree fibres. It follows at once that the projection of a \(\delta\)-pseudo-orbit of \(F\) is a \(\delta\)-pseudo-orbit of \(T\); conversely **every** sequence of lifts of a quotient pseudo-orbit is an \(F\)-pseudo-orbit with the same stepwise errors. Likewise every sequence of lifts of a true quotient orbit is a true \(F\)-orbit, because \(F(x)\) contains the entire next quotient fibre.

**2. Ordinary and periodic shadowing, in both directions and without changing tolerances.** Suppose \(T\) has the \((\delta,\varepsilon)\)-shadowing implication and take an \(F\)-pseudo-orbit \((x_i)\) with step errors below \(\delta\). Its projection is shadowed by \((u_i)=(T^iu_0)\), with \(\bar d(u_i,\pi x_i)<\varepsilon\). For each \(i\), choose \(z_i\in\pi^{-1}(u_i)\) attaining \(d(z_i,x_i)=\bar d(u_i,\pi x_i)\). These lifts form an exact \(F\)-orbit by (1), and shadow \((x_i)\). Conversely, lift any quotient pseudo-orbit arbitrarily, apply shadowing of \(F\), and project the shadowing orbit. The quotient projection is \(1\)-Lipschitz, giving the same \((\delta,\varepsilon)\) implication for \(T\).

For periodic pseudo-orbits, perform the same projection and lifting. If the input pseudo-orbit has period \(n\), while a quotient shadowing orbit has period \(m\), choose a lift \(z_i\) nearest \(x_i\) for \(0\le i<L\), where \(L=\operatorname{lcm}(m,n)\), and repeat those lifts every \(L\) steps. Equation (1) ensures the closing edge is an actual \(F\) transition. Thus the lifted orbit is genuinely periodic of period dividing \(L\), including when its quotient orbit has a different period from the pseudo-orbit. In the converse direction, lift the quotient periodic pseudo-orbit periodically and project its periodic \(F\)-shadowing orbit. Every \((\delta,\varepsilon)\) works in one system exactly when it works in the other; ordinary shadowing and periodic shadowing are therefore each equivalent.

**3. Periodic-point formula.** By induction on \(n\), equivariance gives
\[
F^n(x)=Gf^n(x)=\pi^{-1}(T^n\pi x),\quad n\ge1. \tag{2}
\]
Hence \(x\in F^n(x)\) exactly when \(\pi x\in\operatorname{Fix}(T^n)\). If this fixed-point set is finite, then
\[
P_n(F)=\sum_{u\in\operatorname{Fix}(T^n)}|\pi^{-1}(u)|. \tag{3}
\]
For a free action, all fibres have \(|G|\) points; therefore \(P_n(F)=|G|P_n(T)\) and \(\zeta_F^{\rm pt}=\zeta_T^{|G|}\) whenever these formal zeta functions are defined. Equation (3), rather than constant multiplication, is the exact formula at branch fibres.

**4. The expansivity boundary.** Suppose \(F\) is positively expansive with constant \(\alpha\). If \(T\) were not positively expansive with this constant, there would be distinct quotient points whose forward \(T\)-orbits remain at quotient distance at most \(\alpha\) at all times. At every time select nearest lifts of the two quotient-orbit points. Both sequences are genuine \(F\)-orbits by (1), begin at distinct points, and stay at distance at most \(\alpha\), contradicting expansivity of \(F\). Thus \(T\) is positively expansive.

Now suppose the action is free. Compactness and finiteness give a strictly positive separation
\[
s=\min_{x\in X}\min_{g\in G\setminus\{e\}}d(x,gx)>0
\]
when \(|G|>1\). If \(T\) is positively expansive with constant \(\beta\), take \(\alpha<\min\{s,\beta\}\). Two distinct points of the same quotient fibre are already separated by more than \(\alpha\) at time zero; two points of different fibres have their quotient orbits separated by more than \(\beta\) at some time, and hence every choice of lifted \(F\)-orbits is separated by more than \(\alpha\). This proves the free-action converse; if \(|G|=1\), it is immediate.

**5. Explicit branched counterexample and exact zeta.** Let \(\Sigma=\{0,1\}^{\mathbb N_0}\) with \(\rho(u,v)=2^{-k}\), where \(k\) is the first index of disagreement (and \(\rho(u,u)=0\)). Put \(p=000\ldots\). Form \(X\) from two labelled copies \(\Sigma\times\{0,1\}\) by identifying only \((p,0)\) and \((p,1)\). For points in the same sheet, use \(\rho\); for points in different sheets use \(\rho(u,p)+\rho(v,p)\). This is the compact two-sheet wedge metric. The involution \(R([u,j])=[u,1-j]\) is an isometry, with one fixed branch point. The map \(f([u,j])=[\sigma u,j]\) is continuous, commutes with \(R\), and fixes the branch point. Its quotient is precisely the one-sided binary full shift \((\Sigma,\sigma)\) with metric \(\rho\).

The shift is positively expansive because a first disagreement at index \(k\) becomes distance \(1\) after \(k\) iterations. It also has ordinary and periodic shadowing: for prescribed prefix length \(m\), sufficiently small step errors force the \(m\)-digit words of successive pseudo-orbit points to overlap consistently; taking the diagonal leading digits produces a tracing shift sequence, periodic when the pseudo-orbit is periodic. By step 2, \(F=\{f,Rf\}\) has both shadowing properties.

But \(F\) is **not** positively expansive. For \(k\ge1\), let \(u^{(k)}=0^k10^\infty\) and take \(x_k=[u^{(k)},0]\), \(y_k=[u^{(k)},1]\). They are distinct, have \(d(x_k,y_k)=2^{1-k}\to0\), and satisfy \(F(x_k)=F(y_k)\). Choose equal successors from their common image, then identical forward orbits. Their entire orbitwise separation never exceeds \(2^{1-k}\); no positive expansivity constant exists. Finally, \(\sigma^n\) fixes \(2^n\) binary sequences, exactly one of which is the branch orbit \(p\). The other \(2^n-1\) fixed quotient points have two lifts, so
\[
P_n(F)=1+2(2^n-1)=2^{n+1}-1,
\qquad
\zeta_F^{\rm pt}(z)=\frac{1-z}{(1-2z)^2}. \tag{4}
\]
The bound, counterexample, and the claimed formulas are all established.

## Verification

The main identity (1) is exact and supplies the two-way lifting proof without any appeal to a uniqueness-of-orbits assumption. The least-common-multiple construction checks closure of the periodic lifted orbit; omitting this step would not suffice. The period-dividing counts (3) use fibres and do not count arbitrary path choices. In the two-sheet wedge, the source of non-expansivity is the vanishing separation of paired points approaching the branch point. For \(n=1,2,3\), (4) gives respectively \(3,7,15\), agreeing with the count of one singleton branch fibre and two lifts for each other fixed shift point; the formula for all \(n\) is proved algebraically. No computational experiment is being used as an infinite proof.

## Relationship to prior work

Oliveira, *Periodic Shadowing for Set-Valued Maps* (2026), develops set-valued periodic shadowing and gives a one-directional inheritance construction \(F(x)=\{f(x),R(f(x))\}\) for an isometric involution. The present result identifies the exact **quotient** that governs both kinds of shadowing, proves the converses for that quotient, includes all finite isometry groups and nonfree actions, gives exact periodic point weights, and isolates the sharp loss of positive expansivity at a branch fibre. Zhao and Wang (2026) instead compare a general multifunction with shifts on generalized inverse limits; their main statements do not identify this finite-symmetry quotient or the branched expansivity boundary. Results on preservation of shadowing under general factor maps provide neighboring concepts, but do not by themselves imply the specific simultaneous periodic-shadowing and positive-expansivity classification here.

## Limitations

The equivalences require the **orbit-saturated** transition set \(F(x)=Gf(x)\). They do not hold for arbitrary subrelations of that transition set or for arbitrary set-valued maps. The metric statement uses the canonical minimum quotient metric. The free-action hypothesis is sufficient for the positive-expansivity converse, not claimed necessary in every example. The point-count zeta is not the Artin–Mazur zeta of a uniquely defined multivalued trajectory shift, and no assertion about multiplicity of multivalued orbit realizations is made. This establishes mathematical statements, not bibliographic uniqueness; an equivalent quotient-lifting lemma may exist under other terminology.

## References

1. M. Oliveira, *Periodic Shadowing for Set-Valued Maps*, arXiv:2602.12399v1, first public 12 February 2026, primary MSC 37C50.
2. Y. Zhao and L. Wang, *Shadowing Property and Transitivity of a Set-Valued Map and Its Inverse Limit*, arXiv:2607.17325v1, first public 19 July 2026.
3. Z. Yin, *Shadowing Property for Set-Valued Map and Its Inverse Limit*, arXiv:2412.11221v1, first public 15 December 2024.
4. C. Good, J. Mitchell and J. Thomas, *Preservation of Shadowing in Discrete Dynamical Systems*, arXiv:1907.02446v1, published in Journal of Mathematical Analysis and Applications 485 (2020), 123767.
