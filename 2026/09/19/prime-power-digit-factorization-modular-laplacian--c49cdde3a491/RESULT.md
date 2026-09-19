# Prime-power digit factorization in modular Laplacian dynamics

## Result

Consider a constant-modulus discrete Laplacian cellular automaton on \(\mathbb Z^d\) with a finite mask. Write its translation-polynomial symbol as
\[
P(X)=\sum_{a\in A} c_a X^a\in \mathbb Z[X_1^{\pm1},\ldots,X_d^{\pm1}],
\]
so that a finite-support seed \(U_0\) evolves modulo \(m\) by
\[
U_t=P^tU_0\pmod m.
\]
For the mask Laplacian in arXiv:2609.20416, \(P=\sum_{v\in M}X^v-|M|\).

For an integer \(q\ge1\), let \(D_q\) be spatial dilation on Laurent polynomials,
\[
D_q\!\left(\sum_a c_aX^a\right)=\sum_a c_aX^{qa}.
\]

### Theorem 1: exact prime-power renormalization

Let \(p\) be prime and \(r\ge1\). Define the fixed depth-\(r\) kernel
\[
K_r(P):=P^{p^{r-1}}\pmod{p^r}.
\]
Then for every \(n\ge r-1\),
\[
\boxed{
P^{p^n}\equiv
D_{p^{\,n-r+1}}\!\left(P^{p^{r-1}}\right)
\pmod{p^r}.
}
\]
Equivalently,
\[
P^{p^n}\equiv D_{p^{\,n-r+1}}(K_r(P))\pmod{p^r}.
\]
Thus the prime-power dynamics do not lose all mixed terms as in a finite field. Instead, all large \(p\)-power times are exact spatial dilations of one fixed finite kernel, namely the configuration generated at the base time \(p^{r-1}\).

For a point seed, the entire residue-valued configuration at time \(p^n\) is therefore exactly a \(p^{n-r+1}\)-dilation of the time-\(p^{r-1}\) configuration. This is stronger than support similarity.

### Theorem 2: exact base-\(p\) digit factorization

Write an arbitrary time \(t\ge0\) uniquely as
\[
t=t_<+\sum_{j\ge0} d_j p^{r-1+j},
\qquad
0\le t_<<p^{r-1},\quad d_j\in\{0,\ldots,p-1\}.
\]
Then
\[
\boxed{
P^t\equiv
P^{t_<}
\prod_{j\ge0}
D_{p^j}(K_r(P))^{d_j}
\pmod{p^r}.
}
\]
Only finitely many factors are nontrivial. Hence the complete constant-modulus orbit modulo \(p^r\) admits an exact multiscale factorization controlled by the base-\(p\) digits of time and a single depth kernel \(K_r(P)\).

A useful epoch form follows immediately. For \(n\ge r-1\), \(q=p^{n-r+1}\), and any \(s\ge0\),
\[
\boxed{
U_{p^n+s}=D_q(K_r(P))\,U_s\pmod{p^r}.
}
\]
If
\[
K_r(P)=\sum_z \kappa_zX^z,
\]
then
\[
U_{p^n+s}=\sum_z\kappa_z\,\tau_{qz}U_s\pmod{p^r}.
\]
Thus an entire earlier developmental epoch is reproduced as an exact residue-weighted superposition of widely separated translated copies. When the translated supports are disjoint, the geometric support is exactly the corresponding union; when they overlap, modular cancellation can occur.

## Proof

The only lifting input needed is the following elementary congruence.

**Lemma.** In any commutative integer algebra, if \(A\equiv B\pmod{p^k}\) with \(k\ge1\), then
\[
A^p\equiv B^p\pmod{p^{k+1}}.
\]
Indeed,
\[
A^p-B^p=(A-B)\sum_{i=0}^{p-1}A^{p-1-i}B^i.
\]
The first factor is divisible by \(p^k\). Modulo \(p\), the second factor is congruent to \(pB^{p-1}=0\), because \(A\equiv B\pmod p\). Hence the product is divisible by \(p^{k+1}\).

Now set
\[
q=p^{n-r+1}.
\]
The ordinary Frobenius identity modulo \(p\) gives
\[
P^q\equiv D_q(P)\pmod p.
\]
Apply the lemma successively \(r-1\) times. This yields
\[
(P^q)^{p^{r-1}}
\equiv
D_q(P)^{p^{r-1}}
\pmod{p^r}.
\]
The left side is \(P^{p^n}\), while \(D_q\) is a ring endomorphism, so the right side is
\[
D_q\!\left(P^{p^{r-1}}\right).
\]
This proves Theorem 1.

For Theorem 2, factor
\[
P^t=P^{t_<}\prod_{j\ge0}\left(P^{p^{r-1+j}}\right)^{d_j}
\]
and apply Theorem 1 to each factor. The epoch identity follows by multiplying the special-time identity by \(P^s\); translation polynomials commute.

## Consequences for the observed prime-power signatures

The source paper derives the prime-modulus hierarchy from finite-field Frobenius but explicitly treats prime powers as computational observations. The theorem above gives exact algebraic clocks for every finite mask and every finite seed:

- modulo \(4\):
  \[
  P^{2^n}\equiv D_{2^{n-1}}(P^2)\pmod4,
  \qquad n\ge1;
  \]
- modulo \(8\):
  \[
  P^{2^n}\equiv D_{2^{n-2}}(P^4)\pmod8,
  \qquad n\ge2;
  \]
- modulo \(9\):
  \[
  P^{3^n}\equiv D_{3^{n-1}}(P^3)\pmod9,
  \qquad n\ge1.
  \]

This gives an exact explanation for the binary-like signatures reported for moduli \(4\) and \(8\) and the ternary-like signatures reported for modulus \(9\). The exponent \(r-1\) is a persistent prime-power depth: unlike the field case \(r=1\), the recurrent object is the base kernel \(P^{p^{r-1}}\), not generally the one-step kernel \(P\).

For a composite modulus \(m=\prod_i p_i^{r_i}\), Chinese remaindering projects the dynamics onto prime-power factors. Each projection satisfies its own exact digit factorization. This rigorously supports a mixed-clock interpretation of composite-modulus signatures, but it does not imply one universal full-modulus replication scale unless the component clocks align.

## Relation to prior work and originality boundary

Finite-field Frobenius replication is already established in the source paper and in the author's earlier work on Frobenius revivals. The earlier paper also tabulates empirical replication ladders for \(4,8,9,27\). General additive cellular automata over finite commutative rings and prime-power generalizations of Lucas-type binomial congruences are established topics.

The contribution claimed here is narrower: for the constant prime-power modular Laplacian dynamics highlighted as computational in arXiv:2609.20416v1, the displayed renormalization, digit factorization, and epoch identities give an exact all-mask/all-seed algebraic explanation of the observed prime-power clocks. No broad claim is made that the lifting lemma, prime-power binomial congruences, or additive cellular automata over \(\mathbb Z/p^r\mathbb Z\) are new.

## Verification

`artifacts/verify_prime_power_renormalization.py` checks the special-time identity, the arbitrary-time digit factorization, and the full-epoch identity for several two-dimensional Laplacian-type masks, moduli \(4,8,9\), nontrivial finite seeds, and multiple times. The recorded output is in `artifacts/verification_output.txt`. These computations support the algebra and are not a substitute for the proof above.

## Limitations

The theorem concerns constant-modulus linear dynamics. It does not directly solve the source paper's genuinely time-dependent schedules with changing moduli, nor does it prove density or entropy asymptotics for the carpet-like regimes. Geometric disjoint-copy statements require support separation; the algebraic superposition identity itself does not.

The broad additive-cellular-automaton literature over finite rings is substantial. Some older or inaccessible sources may contain equivalent general polynomial congruences. Accordingly, novelty is claimed only for the source-specific prime-power renormalization and its explicit dynamical consequences described above.

## References

1. M. Nowak-Kępczyk, *Long-Lived Carpet-Like Transients in Time-Dependent Modular Discrete Laplacian Dynamics*, arXiv:2609.20416v1 (2026). https://arxiv.org/abs/2609.20416
2. M. Nowak-Kępczyk, *Frobenius Revivals in Laplacian Cellular Automata: Chaos, Replication, and Reversible Encoding*, arXiv:2511.17389v1 (2025). https://arxiv.org/abs/2511.17389
3. R. A. Dow, *Additive cellular automata and global injectivity*, Physica D 110 (1997), 67–91. https://doi.org/10.1016/S0167-2789(97)00074-2
4. A. Bés, *On Pascal triangles modulo a prime power*, Annals of Pure and Applied Logic 89 (1997), 17–35. https://doi.org/10.1016/S0168-0072(97)85376-6
5. R. Meštrović, *Lucas Type Theorem Modulo Prime Powers*, arXiv:1301.0251 (2013). https://arxiv.org/abs/1301.0251
