# Complete atomic-equation probability spectrum of the six-element permutation group

## Finding
Let \(G=S_3\) be regarded as a **fixed finite first-order group structure**, with multiplication, inversion, identity, and equality, but without named nonidentity elements. Given an atomic equation \(t(\bar x)=s(\bar x)\) with its \(k\ge1\) distinct variables independently uniform in \(G\), write \(P_G(t=s)\) for its satisfaction probability. The complete spectrum of atomic first-order equation probabilities is
\[
\boxed{\left\{P_G(t=s)\right\}=\tfrac13\mathbb Z[1/2]\cap[1/6,1].}
\]
More precisely, for **every** fixed arity \(k\ge2\), the probabilities obtained by equations in at most \(k\) variables, with arbitrary syntactically dummy occurrences allowed, are exactly
\[
\boxed{\left\{\frac{j}{3\cdot2^{k-1}}:\ j\in\mathbb Z,\quad 2^{k-2}\le j\le3\cdot2^{k-1}\right\}.}
\]
For one variable the spectrum is exactly \(\{1/6,1/2,2/3,1\}\). The global spectrum is countable and dense in \([1/6,1]\), but excludes every probability below \(1/6\).

## Assumptions and scope
An equation is atomic in the ordinary group signature \((\cdot,{}^{-1},1)\). Every free variable is sampled independently and uniformly; a variable made syntactically present but semantically unused has no effect on the probability. No individual nonidentity group elements may be used as parameters. An equation \(t=s\) is equivalent to the single word equation \(w=1\), where \(w=ts^{-1}\). We count actual solutions among \(6^k\) tuples, not up to conjugacy or automorphism.

For this theorem the model-theoretic object is the collection of probabilities of **atomic satisfaction sets in one fixed finite structure**, as opposed to a distribution over different groups. The finite-model-theoretic focus motivates classification under MSC2020 03C13; the algebraic word-map representation is the proof technique.

## Proof
**1. Semidirect coordinates.** Identify \(G\) with \(\mathbb F_3\rtimes\mathbb F_2\) where
\[
(a,b)(a',b')=(a+(-1)^b a',\ b+b').
\]
Every group variable is a pair \((a_i,b_i)\), with independent uniform \(a_i\in\mathbb F_3\) and \(b_i\in\mathbb F_2\). For a group word \(w\) on \(k\) variables, induction using this product shows that there are \(e=(e_1,\ldots,e_k)\in\mathbb F_2^k\) and coefficient vectors \(c(b)\in\mathbb F_3^k\), indexed by \(b\in\mathbb F_2^k\), with
\[
w((a_1,b_1),\ldots,(a_k,b_k))=
\left(\sum_{i=1}^k c_i(b)a_i,\quad\sum_{i=1}^k e_ib_i\right).
\]
Put \(\tau_i(b)=(-1)^{b_i}\in\mathbb F_3\), and \(\tau_e(b)=\prod_i\tau_i(b)^{e_i}\). Every word's coefficients satisfy the exact identity
\[
\boxed{\sum_i(\tau_i(b)-1)c_i(b)=\tau_e(b)-1\quad\text{for all }b.}\tag{1}
\]
To verify this, it holds for each generator \(x_i\). For two words having signatures \((e,c)\), \((f,d)\), the product has signature \((e+f,c+\tau_e d)\), and the right side telescopes:
\((\tau_e-1)+\tau_e(\tau_f-1)=\tau_e\tau_f-1\). Inversion follows by multiplying a word with its inverse. Thus (1) holds for all words.

**2. All solutions of (1) are word-realizable.** Consider even-parity words, meaning words with \(e=0\). Their coefficient arrays form an additive \(\mathbb F_3\)-subspace of
\[
K=\{c:\ \sum_i(\tau_i(b)-1)c_i(b)=0\text{ for every }b\}.
\]
Conjugating such a word by \(x_\ell\) multiplies its coefficient vector at \(b\) by \(\tau_\ell(b)\). Hence attainable arrays form a module over the function ring \(R=\mathbb F_3[\mathbb F_2^k]\cong\prod_{b\in\mathbb F_2^k}\mathbb F_3\), where the \(\ell\)-th generator acts as the function \(\tau_\ell\). Because \(2\) is invertible in \(\mathbb F_3\), the idempotent
\[
 p_b=2^{-k}\prod_{i=1}^k(1+\tau_i(b)\tau_i)
\]
selects exactly the \(b\)-coordinate. This projector is realizable by additions and conjugations of even-parity words.

For the fixed coordinate \(b\), let \(\delta(b)=(\tau_i(b)-1)_i\). The allowed fiber is \(K_b=\ker(\delta(b)\cdot -)\), of dimension \(k\) at \(b=0\), and \(k-1\) at \(b\ne0\). Two families of **actual even-parity words** span these fibers: \(x_i^2\), with coefficient vector \((1+\tau_i(b))u_i\), and commutators \([x_i,x_j]=x_ix_jx_i^{-1}x_j^{-1}\), with vector
\[
 (1-\tau_j(b))u_i+(\tau_i(b)-1)u_j.
\]
Here \(u_i\) is the standard coordinate vector. If \(b=0\), squares span all \(k\) coordinates. If \(b\ne0\), squares span the coordinates with \(b_i=0\), while commutators among the coordinates with \(b_i=1\) span their sum-zero hyperplane. Thus they span the full \(K_b\) in every case. Applying the projectors \(p_b\) proves that every array in \(K\) is realized by an even-parity word.

For any fixed \(e\), take the word \(w_e=\prod_i x_i^{e_i}\). Its coefficients satisfy (1). Every other solution of (1) differs from those coefficients by an array in \(K\), realized by an even-parity word. Multiplying by this word realizes the desired coefficients without changing \(e\). **Therefore (1) is both necessary and sufficient.**

**3. Exact probability at a fixed arity.** Conditional on a sign vector \(b\), the word can equal the identity only when \(\sum_i e_i b_i=0\) in \(\mathbb F_2\). Among such vectors, if \(c(b)=0\), every rotation assignment is a solution; otherwise precisely one-third are solutions, since a nonzero \(\mathbb F_3\)-linear functional is uniformly distributed.

If \(e=0\), all \(2^k\) sign vectors are eligible. Let \(z\) be the number for which \(c(b)=0\). Then
\[
 P_G(w=1)=\frac13+\frac{2z}{3\cdot2^k}.
\]
If \(e\ne0\), precisely \(2^{k-1}\) sign vectors are eligible and
\[
 P_G(w=1)=\frac16+\frac{2z}{3\cdot2^k}.
\]
For \(k\ge2\), each eligible fiber \(K_b\) has positive dimension (at \(b=0\), dimension \(k\), otherwise \(k-1\)). By Step 2, independently prescribe \(c(b)=0\) or any nonzero allowed vector at every eligible \(b\). Consequently, in the first case every integer \(0\le z\le2^k\) occurs, and in the second every integer \(0\le z\le2^{k-1}\) occurs. These give the contiguous integer-numerator intervals
\[
 [2^{k-1},3\cdot2^{k-1}]\quad\text{and}\quad
 [2^{k-2},3\cdot2^{k-2}]
\]
in the common denominator \(3\cdot2^{k-1}\). They overlap, and their union gives **every** numerator from \(2^{k-2}\) through \(3\cdot2^{k-1}\), proving the fixed-arity formula.

For \(k=1\), a word is a power \(x^m\). Of the six elements, one has order \(1\), three have order \(2\), and two have order \(3\), giving probabilities \(1/6,1/2,2/3,1\). Taking the union over arities yields precisely \(\frac13\mathbb Z[1/2]\cap[1/6,1]\). Density in the stated interval follows from density of dyadic rationals. This also proves sharpness of the lower bound.

## Verification
Run `python3 s3_equational_checker.py` from this directory. The self-contained standard-library checker enumerates all \(972\) binary-variable word functions as a finite closure under generators (inverses are their fifth powers since \(S_3\) has exponent six), reproduces the six values \(\{1/6,1/3,1/2,2/3,5/6,1\}\), independently checks all \(124\) local spanning ranks for \(2\le k\le6\), and compares the coefficient-form evaluation with direct multiplication on \(828\) concrete group assignments. The finite computations check the representation's low-arity consequences; the arbitrary-arity result follows from the algebraic module proof.

## Relationship to prior work
Cardó introduced the equational probabilistic spectrum and explicitly listed the complete spectrum of \(S_3\) as an open example in Section 4 and the conclusion of *Probabilistic equational spectrum, primality and approximation in finite algebras* (arXiv:2604.08446v1, publicly submitted 2026-04-09). That work computes one particular family of word-equation probabilities, but not the complete range. The present proof uses the elementary semidirect decomposition and character-localized word coefficients to determine the whole spectrum, including every fixed-arity value.

Schneider and Thom, *Word maps with constants on symmetric groups* (arXiv:2206.11956, published 2023/2024), study word-map image bounds for variable symmetric groups and polynomial maps **with named group constants**; their stated theorems do not assert this constant-free, fixed-\(S_3\) equation-probability classification. Standard Fox-type coefficient identities motivate Step 1 but do not supply the explicit spectrum without the surjectivity and zero-pattern arguments of Steps 2–3.

## Limitations
The theorem concerns atomic equations in the parameter-free group language on the one fixed six-element group; it is not a classification of arbitrary first-order formulas, formulas with named nonidentity parameters, more general groups, or word-length complexity. The algebraic sufficiency argument is an unrestricted mathematical proof, whereas the checker covers finitely many arities and examples. A historically overlooked equivalent description of all word maps of \(S_3\) could imply the result; priority beyond the inspected sources requires further external review. The result has not received an independent scientific audit.

## References
1. Carles Cardó, *Probabilistic equational spectrum, primality and approximation in finite algebras*, arXiv:2604.08446v1 (2026-04-09), Sections 2–4 and concluding open problems. https://arxiv.org/abs/2604.08446 ; https://arxiv.org/html/2604.08446 .
2. Jakob Schneider and Andreas Thom, *Word maps with constants on symmetric groups*, arXiv:2206.11956 (2022), published in *Mathematische Nachrichten* (2023/2024). https://arxiv.org/abs/2206.11956 .
3. Carles Cardó, *Minimal probabilistic spectrum grupoids*, arXiv:2603.19487v1 (2026-03-19). https://arxiv.org/abs/2603.19487 .
