# No ideal-simple skew brace of order p^2 q for distinct odd primes; target sharpness is impossible

## Context
Classification of finite simple skew left braces is an open demand in the
set-theoretic Yang–Baxter program (Vendramin Problem 2.25; Guarnieri–Vendramin,
Smoktunowicz). Order-restricted rigidity with a sharp arithmetic boundary is
the recognized incremental form. The admitted target claimed: for distinct odd
primes p,q with q not dividing p(p+1), every ideal-simple skew brace of order
p^2 q is of abelian type with cyclic circle group (via socle-filtration /
matched-pair), plus sharpness witnessed by an odd-p^2 q boundary simple with
q | p+1. This record establishes that the conjunction is false as stated.

## Definitions
A skew (left) brace is (B,+,circ) with (B,+),(B,circ) groups and
a circ (b+c) = a circ b - a + a circ c. Put lambda_a(b) = -a + a circ b;
lambda:(B,circ) -> Aut(B,+) is a homomorphism. A subgroup I <= (B,+) with
lambda_a(I)=I for all a is a left ideal; an ideal is a left ideal normal in
both (B,+) and (B,circ). Ideal-simple means |B|>1 with no nonzero proper
ideal.

## Result
Let p,q be distinct odd primes and |B| = p^2 q. Then B always carries a proper
nonzero ideal: of order q if q > p, of order p^2 if q < p. Hence no
ideal-simple skew brace of that order exists; the rigidity clause holds
vacuously over the empty class. In particular no ideal-simple boundary
example of odd order p^2 q with q | p+1 exists, so the claimed sharpness
witness cannot exist. Among odd primes the condition q ∤ p+1 is inessential
(simplicity fails on both sides); oddness itself is essential (order 12 admits
simples where Sylow uniqueness fails).

## Proof / evidence
Lemma 1 (left ideal => circ-subgroup; Damele Prop 2.1): for h,k in H,
h circ k = h + lambda_h(k) in H; circ-inverse is lambda_h^{-1}(-h) in H.
Lemma 2 (Sylow counting at order p^2 q): n_p | q, n_p = 1 mod p so
n_p in {1,q} with n_p=q only if q = 1 mod p; n_q | p^2, n_q = 1 mod q so
n_q in {1,p,p^2} with non-uniqueness only if p = 1 mod q or p^2 = 1 mod q.
Lemma 3 (characteristic Sylow is an ideal; Acri–Bonatto Lemma 2.1 mechanism):
if H char (B,+) has Sylow order forced unique in every group of order p^2 q,
then H is lambda-invariant and +-normal, hence a left ideal, hence by
Lemma 1 a circle-subgroup of Sylow order, hence the unique Sylow of
(B,circ), hence normal there.
Case q>p: n_q=1 in every group of order p^2 q. Candidates {1,p,p^2}:
p = 1 mod q needs q | p-1, impossible as 0<p-1<q; p^2 = 1 mod q needs
q | (p-1)(p+1); q | p-1 impossible, q | p+1 gives q <= p+1 i.e. q=p+1 since
q>p, impossible by parity (p odd => p+1 even >2, q odd prime). Unique Sylow
q-subgroup Q char (B,+) of order q is an ideal by Lemma 3.
Case q<p: n_p=1 since n_p=q would need q = 1 mod p, impossible as 1<q<p.
Unique Sylow p-subgroup P char (B,+) of order p^2 is an ideal by Lemma 3.
Corollary (no odd boundary witness): q | p+1 with q odd gives
q <= (p+1)/2 < p, hence in case q<p with order-p^2 ideal.
Remark: q<p leg uses no parity; p=2 exception is real (order 12, n_3 in
{1,4}; simples S_{12,22}, S_{12,23} with additive A4).
Computational check (not the proof): stdlib script checks all 1980 distinct
odd prime pairs below 200 (990 each side, 58 odd boundary with q | p+1) plus
the order-12 exception; VERIFY_OK.

## Limitations
Disproof, not a construction: establishes emptiness of the odd simple class
and impossibility of the odd boundary witness; does not classify non-simple
braces (Acri I/II) nor address p=2. Vacuous truth of the rigidity clause is
in classical logic; the conjunction with sharpness is false. Computation
below 200 is a check only; the proof is general. If sharpness is
reinterpreted to allow p=2, order-12 simples (3 | 2+1) witness sharpness with
oddness dropped; the admitted odd-p^2 q sense remains impossible.

## Reproducibility
Pencil proof above is self-contained given Sylow's theorem, Lemma 1, and the
Acri–Bonatto characteristic-Sylow mechanism. Replay:
`python3 output/artifacts/verify_sylow_chase.py` prints counters and
VERIFY_OK (stdlib only).

## References
- Acri–Bonatto, Skew braces of size p^2 q I: abelian type, arXiv:2004.04291
  (Lemma 2.1, holomorph method).
- Acri–Bonatto, Skew braces of size p^2 q II: non-abelian type,
  arXiv:2004.04232.
- Byott, On a family of simple skew braces, arXiv:2405.16154 (order p^p q
  family; order-12 pair).
- Damele, Simple skew braces with cyclic Sylow subgroups, arXiv:2607.17125
  (Props 2.1–2.5, Thms A/B/C; order-12 simples).
- Vendramin, Problems on Skew Left Braces (Problem 2.25: classify finite
  simple skew braces).
