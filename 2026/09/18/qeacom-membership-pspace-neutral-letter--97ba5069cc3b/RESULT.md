# QEACom membership is PSPACE-complete even for neutral-letter NFAs

## Statement

Let `QEACom` be the lm-pseudovariety introduced by Göller and Manuel: a syntactic stamp belongs to `QEACom` when its stable semigroup belongs to `EACom`, where `EACom` is defined by the identities
\[
epx^{\omega+1}qf=epx^\omega qf,
\qquad
epxyqf=epyxqf,
\]
for idempotents \(e,f\) and arbitrary \(p,q,x,y\) in the semigroup.

The following two facts hold.

**Theorem 1 (neutral-letter collapse).** If a regular language \(L\subseteq\Sigma^+\) has a neutral letter, then
\[
\eta_L\in \mathbf{QEACom}
\quad\Longleftrightarrow\quad
S(L)\text{ is aperiodic and commutative}.
\]
Equivalently, for some threshold \(t\), membership in \(L\) depends only on the truncated Parikh vector
\[
\bigl(\min\{|w|_a,t\}\bigr)_{a\in\Sigma\setminus\{c\}},
\]
where \(c\) is a neutral letter.

Consequently, every neutral-letter language in `QEACom` has a sharp constant-versus-logarithmic-jump statement in the source paper's asymptotic conventions: either \(\operatorname c(L)\in O(1)\), or else \(\operatorname c(L)\in O(\log n)\) and \(\operatorname c(L)\in\Omega_{\mathrm{HL}}(\log n)\), where the latter is Hardy--Littlewood Omega (a logarithmic lower bound for infinitely many input lengths). Equivalently, the second case is not \(o(\log n)\).
The first case occurs exactly when \(L\) is idempotent (commutativity is already forced by `QEACom`). For example,
\[
L_{\ge2}=\{w\in\{a,\$\}^+:|w|_a\ge2\}
\]
has neutral letter \(\$\), lies in `QEACom`, is not idempotent, and therefore has an \(O(\log n)\) upper bound together with a Hardy--Littlewood \(\Omega(\log n)\) lower bound.

**Theorem 2 (decision complexity).** Given an NFA \(\mathcal A\), deciding whether the syntactic morphism of \(L(\mathcal A)\) belongs to `QEACom` is `PSPACE`-complete under logarithmic-space reductions. Hardness remains true when the input is restricted to NFAs whose language has a neutral letter.

## Proof of Theorem 1

For a neutral-letter language, Göller and Manuel observe that the syntactic semigroup is a monoid and that its stable semigroup is the entire syntactic semigroup. Let \(1\) be its identity. In the two `EACom` identities set \(e=f=p=q=1\). They become
\[
x^{\omega+1}=x^\omega,
\qquad
xy=yx.
\]
Hence a neutral-letter `QEACom` language has an aperiodic commutative syntactic monoid.

Conversely, an aperiodic commutative monoid satisfies the two identities immediately: commute the factors in the second identity, and use \(x^{\omega+1}=x^\omega\) in the first. Thus the stable semigroup is in `EACom`.

For the truncated-Parikh formulation, let \(M=S(L)\). Since \(M\) is finite and aperiodic, there is a common \(t\) such that \(m^t=m^{t+1}\) for every \(m\in M\). Since \(M\) is commutative and the neutral letter maps to the identity,
\[
\eta_L(w)=\prod_{a\ne c}\eta_L(a)^{\min(|w|_a,t)}.
\]
Thus the truncated Parikh vector determines membership. Conversely, any language determined by such a vector is recognized by a finite direct product of capped-addition monoids \(\{0,1,\ldots,t\}\); these monoids are aperiodic and commutative, so the syntactic monoid, as a divisor, is as well.

For the circuit dichotomy, Proposition 6.8 of Göller--Manuel gives the `QEACom` upper bound \(O(\log n)\). Their Corollary 4.16 says that a neutral-letter regular language has constant circuit complexity exactly when it is idempotent and commutative. If a neutral-letter `QEACom` language is not idempotent, it is therefore not in `QEJ1`; Theorem 4.17 supplies a Hardy--Littlewood \(\Omega(\log n)\) lower bound, i.e. the lower bound holds for infinitely many input lengths.

## Proof of Theorem 2: PSPACE upper bound

Let \(\mathcal A=(Q,\Sigma,\Delta,q_0,F)\) be an NFA. Use the transition-matrix morphism
\[
\mu:\Sigma^+\to\mathbb B^{Q\times Q}
\]
and let \(T=\mu(\Sigma^+)\). As in the proof of Göller--Manuel Proposition 5.2, write
\[
\eta_L=\beta\circ\mu.
\]
Their Claims 2 and 3 give polynomial-space procedures for (i) deciding whether a Boolean transition matrix lies in \(\operatorname{stab}(\mu)\), and (ii) deciding whether two stable transition matrices have the same image under \(\beta\).

It remains only to test the two `EACom` identities. Deterministically enumerate polynomial-space representatives for \(e,f,p,q,x,y\) in \(\operatorname{stab}(\mu)\). Idempotent syntactic elements may be represented by idempotent transition matrices: if \(\beta(t)\) is idempotent then the unique idempotent power \(t^\omega\) is a stable representative of the same syntactic element.

For the \(\omega\)-identity, an idempotent power of any \(t\in T\) occurs among the first \(|T|\) powers. Since \(|T|\le2^{|Q|^2}\), one can generate powers of \(t\) sequentially, using a \(|Q|^2\)-bit counter and one Boolean matrix, until an idempotent is found. This uses polynomial space. The two sides of each identity are then compared with the polynomial-space \(\beta\)-equality test. Exhaustive enumeration uses exponential time but only polynomial space. Hence `QEACom` membership for NFAs is in `PSPACE`.

## Proof of Theorem 2: PSPACE hardness

Use the special NFA-universality instances in Göller--Manuel Proposition 5.3. From a `PSPACE`-hard instance one obtains, in logarithmic space, an NFA \(\mathcal A\) over \(\Sigma\) such that either
\[
L(\mathcal A)=\Sigma^+
\]
or
\[
L(\mathcal A)=\Sigma^+\setminus\{w\}
\]
for one word \(w\in\Sigma^+\).

Introduce fresh letters \(c,d\) and put \(\Delta=\Sigma\cup\{c,d\}\). Define
\[
K_{\mathcal A}
=
\Delta^*\setminus
\{xcd:x\in\Sigma^+\setminus L(\mathcal A)\}.
\]
Equivalently,
\[
K_{\mathcal A}
=
(\Delta^*\setminus\Sigma^+cd)\;\cup\;L(\mathcal A)cd.
\]
The first term is recognized by a constant-size DFA once letters are grouped as \(\Sigma,c,d\), and the second is obtained by appending two transitions to \(\mathcal A\). Hence an NFA for \(K_{\mathcal A}\) is constructible in logarithmic space without complementing \(\mathcal A\).

Now introduce a fresh symbol \(\$\), let \(\varphi\) erase \(\$\), and construct an NFA \(\mathcal B\) for
\[
L(\mathcal B)=\varphi^{-1}(K_{\mathcal A})\cap\Gamma^+,
\qquad
\Gamma=\Delta\cup\{\$\},
\]
by adding a \(\$\)-loop to every state. Thus \(\$\) is a neutral letter.

If \(L(\mathcal A)=\Sigma^+\), then \(K_{\mathcal A}=\Delta^*\) and \(L(\mathcal B)=\Gamma^+\), whose syntactic monoid is trivial, hence in `QEACom`.

If \(L(\mathcal A)=\Sigma^+\setminus\{w\}\), then
\[
K_{\mathcal A}=\Delta^*\setminus\{wcd\}
\]
and
\[
L(\mathcal B)=\Gamma^+\setminus\varphi^{-1}(wcd).
\]
This language is not commutative: \(wcd\) is rejected while \(wdc\) is accepted. Hence the syntactic images of \(c\) and \(d\) do not commute. By Theorem 1, \(L(\mathcal B)\notin\mathbf{QEACom}\). This proves `PSPACE` hardness even on neutral-letter instances.

## Relation to prior work and originality boundary

Göller and Manuel introduced `QEACom`, characterized its languages, and proved that `QEACom` gives an \(O(\log n)\) circuit upper bound. They also proved `PSPACE`-completeness of deciding **constant** circuit complexity for NFA input, but do not state the complexity of deciding `QEACom` membership. Their neutral-letter observation and their polynomial-space transition-semigroup machinery are explicit ingredients of the proof above.

Classical work already shows `PSPACE`-completeness for aperiodicity/star-freeness questions for finite automata (for example Bernátsky, 1997), and commutative star-free languages have independent structural characterizations. No novelty is claimed for those generic facts. The claimed contribution is the `QEACom`-specific membership classification, including hardness under the neutral-letter restriction, together with the resulting neutral-letter \(O(1)\) versus not-\(o(\log n)\) jump inside the \(O(\log n)\) envelope of the newly introduced class.

To the best of our knowledge, searches for `QEACom` together with NFA membership, PSPACE, neutral letters, `EACom`, commutative aperiodicity, and equivalent syntactic-monoid terminology did not locate this theorem. Because `QEACom` was introduced in a very recent preprint, a near-simultaneous observation or a subsequent revision remains a material originality risk.

## Limitations

The result concerns membership in `QEACom`, not membership in the full class of regular languages having \(O(\log n)\) circuits; Göller and Manuel already give examples with \(O(\log n)\) complexity outside `QEACom`. No lower complexity bound is claimed for other input representations such as a minimal DFA. The neutral-letter collapse is elementary once the defining identities are written in a monoid, and is used here mainly to obtain the restricted hardness theorem and the circuit dichotomy.

## Verification artifact

`artifacts/verify_neutral_qeacom.py` checks two finite examples. It computes the transition monoid of the threshold language \(|w|_a\ge2\) and confirms that it is aperiodic and commutative but not idempotent. It also computes the transition monoid of the language accepting every word except those whose deletion of \(\$\) equals `acd`; the monoid is aperiodic but noncommutative, with `cd` and `dc` separated after prefix `a`. The artifact is a finite sanity check and is not used in place of the general proof.

## References

1. Stefan Göller and Amaldev Manuel, *Rational Reductions and Regular Languages of Constant Circuit Complexity*, arXiv:2609.18484 (2026). https://arxiv.org/abs/2609.18484
2. László Bernátsky, *Regular expression star-freeness is PSPACE-complete*, Acta Cybernetica 13(1), 1--21 (1997). https://acta.bibl.u-szeged.hu/12575/
3. Aidan Delaney, Gem Stapleton, John Taylor, and Simon Thompson, *On the expressiveness of spider diagrams and commutative star-free regular languages*, Journal of Visual Languages & Computing 24(4), 273--288 (2013), DOI: 10.1016/j.jvlc.2013.02.001.
