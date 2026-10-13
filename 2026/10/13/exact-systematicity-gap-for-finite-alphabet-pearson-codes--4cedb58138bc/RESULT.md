# Exact systematicity gap for finite-alphabet Pearson codes
## Finding
Fix the ordered signal alphabet \(Q=\{0,1,\ldots,q-1\}\), with \(q\ge2\), and an integer \(k\ge1\). A word is Pearson-admissible when it is not constant, and two distinct words cannot be positive-affine images of one another. Write \(r_{\mathrm{free}}(q,k)\) for the smallest integer \(r\ge0\) such that a Pearson code of length \(k+r\) contains \(q^k\) words. Write \(r_{\mathrm{sys}}(q,k)\) for the smallest \(r\) for which there is an encoder \(E:Q^k\to Q^{k+r}\) of the form \(E(u)=(u,f(u))\) whose image is Pearson-admissible.

The exact values are
\[
r_{\mathrm{sys}}(q,k)=\begin{cases}1,&q=2,\\2,&q\ge3,\end{cases}
\qquad
r_{\mathrm{free}}(q,k)=\begin{cases}1,&q=2\text{ or }k\ge2,\\2,&q\ge3\text{ and }k=1.\end{cases}
\]
Consequently, for every \(q\ge3\) and \(k\ge2\), preserving the information coordinates costs exactly one further symbol beyond the unrestricted minimum: \(r_{\mathrm{sys}}(q,k)-r_{\mathrm{free}}(q,k)=1\).

## Assumptions and scope
The elements of \(Q\) are ordinary ordered real signal levels, not residue classes. A Pearson code \(C\subseteq Q^n\) must contain no constant vector, and must have no distinct \(x,y\in C\) with
\[
y=ax+b\mathbf{1},\qquad a>0,\quad b\in\mathbb R.
\]
This is the zero-Pearson-distance confusability relation. An unrestricted encoder is any injection of all \(q^k\) messages into such a code. A systematic encoder retains all \(k\) message coordinates unchanged in preassigned positions; permutation of coordinates reduces this to the displayed form. The quantities above count *whole alphabet symbols* beyond the \(k\) message symbols, not information-theoretic real-valued redundancy. Both encoders are fixed-to-fixed with every message admitted; variable-to-fixed schemes and noisy-channel error exponents are outside the claim.

## Proof
**Step 1: An unavoidable symbol for every encoder.** A length-\(k\) code with \(q^k\) distinct words would equal all of \(Q^k\). It would therefore contain a constant word, which is inadmissible. Thus both minima are at least one.

**Step 2: An unrestricted length-three supply.** Let \(m=q-1\) and
\[
F(m)=\bigl|\{(a,b)\in\{1,\ldots,m\}^2:\gcd(a,b)=1\}\bigr|.
\]
Consider the length-three primitive Pearson set
\[
P_{q,3}=\{x\in Q^3:\min_i x_i=0,\ \max_i x_i>0,\ \gcd(x_1,x_2,x_3)=1\}.
\]
It contains exactly \(3F(m)+3\) words: a word has either exactly one zero coordinate (three choices, with the other two positive coprime entries) or exactly two zero coordinates (three choices, with its positive entry necessarily one). The normalization by subtracting the minimum and dividing by the positive-coordinate gcd shows that each positive-affine equivalence class of nonconstant words contains at most one member of \(P_{q,3}\). More explicitly, if two primitive words satisfy \(y=ax+b\mathbf{1}\), then their zero minima force \(b=0\), and integer primitivity forces \(a=1\); hence \(y=x\).

Every noncoprime ordered pair of positive integers at most \(m\) has a common prime divisor, so the number of such pairs is no greater than
\[
\sum_{\substack{p\le m\\p\text{ prime}}}\left\lfloor\frac{m}{p}\right\rfloor^2
\le m^2\left(\frac14+\sum_{j=1}^{\infty}\frac1{(2j+1)^2}\right)
<\frac{m^2}{2}.
\]
The final strict inequality follows from \((2j+1)^2>4j(j+1)\) and \(\sum_{j\ge1}1/(j(j+1))=1\). Thus \(F(m)>m^2/2\) and
\[
|P_{q,3}|=3F(m)+3>\frac32m^2+3\ge(m+1)^2=q^2,
\]
where the last inequality is equivalent to \((m-2)^2\ge0\). Choose any \(q^2\) distinct primitive triples as a set \(B\). For \(k\ge2\), the Cartesian family
\[
C_{q,k}=\{(b,v):b\in B,\ v\in Q^{k-2}\}\subseteq Q^{k+1}
\]
has exactly \(q^k\) members. If two codewords in this family were positive-affine related, their initial triples would first have to be equal because \(B\) has one representative per equivalence class. The common triple has at least two different entries, so its only positive-affine self-map is the identity; this then forces equality of the suffixes. Hence \(C_{q,k}\) is a Pearson code, proving \(r_{\mathrm{free}}(q,k)=1\) for every \(k\ge2\).

At \(k=1\), all nonconstant length-two words fall into exactly two classes under increasing affine maps: increasing and decreasing pairs. Therefore a length-two Pearson code has size at most two, and cannot encode \(q\ge3\) messages. The two fixed reference symbols in \((u,0,1)\) give a Pearson code for all \(q\) at length three; so \(r_{\mathrm{free}}(q,1)=2\) for \(q\ge3\).

**Step 3: A universal systematic one-check obstruction.** Suppose \(q\ge3\) and a systematic encoder with only one extra symbol exists. Its codewords on the \(q\) constant messages are
\[
E(a,a,\ldots,a)=(a,a,\ldots,a,t_a),\qquad a\in Q.
\]
Pearson admissibility demands \(t_a\ne a\). Thus each of these words is either upward oriented (\(t_a>a\)) or downward oriented (\(t_a<a\)). Among at least three constant messages, two have the same orientation. If these correspond to distinct levels \(a,b\), the positive affine map
\[
x\longmapsto \lambda x+\beta,\qquad
\lambda=\frac{t_b-b}{t_a-a}>0,\qquad \beta=b-\lambda a,
\]
takes the first codeword to the second, a contradiction. Hence \(r_{\mathrm{sys}}(q,k)\ge2\) for \(q\ge3\), irrespective of \(k\).

**Step 4: Sharp constructions.** For any \(q\ge2\), the codewords \(E(u)=(u,0,1)\) are nonconstant. Since any positive affine map fixing the final two coordinates zero and one is the identity, this is a systematic Pearson code with two extra symbols. For binary \(q=2\), instead use the one-symbol check \(f(u)=1\) only when \(u\) is the all-zero message and \(f(u)=0\) otherwise. The output is always nonconstant; two nonconstant binary words are positive-affine related only if identical. This yields a systematic one-check code for every \(k\ge1\), and thus also establishes the unrestricted binary upper bound. Combining the preceding bounds proves the formulas.

## Verification
The accompanying dependency-free Python program `verify.py` enumerates primitive triples for \(2\le q\le13\), checks \(|P_{q,3}|=3F(q-1)+3>q^2\) in each case, and independently compares gcd-normalized representatives with exact rational min/max normalizations. For \(2\le q\le7\), it also independently counts all positive-affine classes among every ternary-length word over \(Q\). It constructs the unrestricted Cartesian code for \(2\le q\le5\), \(2\le k\le4\), and tests every produced codeword against both equivalence signatures. Finally, it verifies the two orientation classes of one-check encodings of constant payloads for \(2\le q\le5\). These are finite corroborations only; the argument above proves all integer parameters.

Run `python3 verify.py`; the expected final line is:

`VERIFY_OK exact_r_sys_q_ge_3=2 exact_r_free_q_ge_3_k_ge_2=1 exact_r_free_q_ge_3_k_1=2 exact_r_binary=1`

## Relationship to prior work
Weber, Schouhamer Immink and Blackburn introduced and characterized optimal maximum-cardinality Pearson codes, including the canonical primitive set and its exact cardinality for general \(q,n\). Their bound already determines the unrestricted maximum number of codewords at every fixed block length. This finding does not claim to improve that result; the primitive triple supply is an elementary specialization used to exhibit a one-extra-symbol encoder for every message length of at least two symbols.

Weber, Swart and Schouhamer Immink gave the natural fixed-to-fixed systematic construction with two reserved reference positions, and studied variable-to-fixed schemes. That two-reference construction is prior work. The additional point proved here is that, for full-alphabet systematic fixed-to-fixed encoding and at least three signal levels, no one-check construction exists—while the unrestricted encoder does use one extra symbol as soon as there are two information symbols. Thus an exact one-symbol **systematicity penalty**, rather than a new large Pearson code or an improved reference construction, is the claimed result.

## Limitations
The exact lower bound concerns encoders that leave every information coordinate unchanged and represent *all* possible messages. It does not apply to systematic encoders that omit some messages, use constrained message alphabets, change the alphabet size, permit variable block lengths, or relax positive-affine indistinguishability. It says nothing about Euclidean error performance, Gaussian noise, or efficient table-free nonsystematic encoding. The explicit universal unrestricted construction can require a lookup table of \(q^2\) primitive triples; no uniform efficient implementation bound is claimed. The 2015 cardinality theorem covers much of the existence side; any separate historical source proving the systematic impossibility would limit the novelty of the combined boundary.

## References
1. J. H. Weber, K. A. Schouhamer Immink and S. R. Blackburn, “Pearson Codes,” arXiv:1509.00291v1 (first submitted 2015-09-01), later IEEE Transactions on Information Theory 62(1), 131–135 (2016), DOI: 10.1109/TIT.2015.2490219.
2. J. H. Weber, T. G. Swart and K. A. Schouhamer Immink, “Simple Systematic Pearson Coding,” IEEE International Symposium on Information Theory, 385–389 (2016), DOI: 10.1109/ISIT.2016.7541326; lawful accepted author manuscript at TU Delft.
