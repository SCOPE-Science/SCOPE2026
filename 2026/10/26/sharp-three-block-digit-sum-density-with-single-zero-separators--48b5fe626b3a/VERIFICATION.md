---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For every a,b,c>=1 with binary t=1^c 0 1^b 0 1^a and w=a+b+c, digitwise addition gives s_2(n+t)-s_2(n)=w-K where K counts all outgoing carries, including above t. With independent fair binary n digits, the weighted two-state matrices M_1(u)=[[1/2,u/2],[0,u]] and M_0(u)=[[1,0],[1/2,u/2]] give (P,R)=(1,0)M_1(u)^a M_0(u)M_1(u)^b M_0(u)M_1(u)^c; an outgoing high carry adds geometric pgf 1/(2-u). R has degree at most w+2, and its leading coefficient is exactly 1/8 because all carries require starting a carry at the lowest one-bit and surviving the two zero separators (three independent probability-1/2 events). Ending the final one-bit with no carry forces its incoming carry zero, giving deg(P)<=w. Therefore Pr(K>w)=R(2)/2^(w+1)-1/8 and c_t=9/8-R(2)/2^(w+1). Evaluating M_1(2)^a=[[2^-a,(2/3)(2^a-2^-a)],[0,2^a]], M_0(2)=[[1,0],[1/2,1]] and multiplying yields (27*2^(a+b+c)/2)*R(2)=16X²Y²Z²-4X²Y²-X²Z²-2X²-4Y²Z²+Y²-2Z²-4 (X=2^a,Y=2^b,Z=2^c), verified independently with symbolic exact algebra. This gives c_t=(115+32A+8B+32C+16AB-8AC+16BC+32ABC)/216 with A=4^-a,B=4^-b,C=4^-c. The three derivatives of the numerator w.r.t A,B,C are 32+16B-8C+32BC, 8+16A+16C+32AC, and 32+16B-8A+32AB, strictly positive on [0,1/4]^3. Hence strict decrease with each integer length, infimum 115/216 attained only in the joint limit a,b,c→∞. Exact independent brute enumeration of 2^(a+b+c+2) low residues with analytically integrated infinite high-bit carry tail matched all 27 triples 1<=a,b,c<=3; a=b=c=1 gives 5/8 and 2 gives 567/1024. Finite checks are corroborative, algebra supplies the infinite proof.

## originality

PASS

The precise three-parameter formula and sharp finite-block inequality for the canonical unit-zero-gap three-block family are not stated in the inspected primary results. The carry-state transfer framework, reverse-digit symmetry, and limiting constant 115/216 are prior work. Sobolewski–Spiegelhofer prove the two-block threshold >5/9 (their §5.3), explicitly formulate general N-block lower bound as Conjecture 13 and evaluate its N=3 infinite-block constant in Proposition 16; their §6.1 says unrestricted block monotonicity can fail and gives cases. Cheng’s 2026 all-t bound c_t>=1/2+2^(-2s_2(t)-1) is strictly weaker than 115/216 for large total block lengths and does not explicitly identify this finite-parameter formula. No dominating theorem located by 3 independent Resultary searches, targeted public web and SCOPE file search. This is best-of-knowledge, not historical priority certification; inability to read all of Cheng is documented.

## value

PASS

The three one-block family with both zero gaps of minimal possible positive length is the canonical natural slice of Sobolewski–Spiegelhofer’s Conjecture 13. The exact 115/216 limiting value was already known, but proving it is the sharp infimum for every finite positive a,b,c on that slice settles an infinite family of genuinely proposed inequalities; proving strict monotonicity in each block is meaningful because unrestricted length-monotonicity fails for other block patterns (2024 §6.1). The full correction polynomial quantifies the approach along independent lengths and reveals c_(2,2,2)=567/1024<5/9, so two-block sharp bounds do not persist after adding one one-block. This is a narrowly scoped, intrinsically motivated exact theorem, not an arbitrary finite check or claim to settle general three-block shifts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
