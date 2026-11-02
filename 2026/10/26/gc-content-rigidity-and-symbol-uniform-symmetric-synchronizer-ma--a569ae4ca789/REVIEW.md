# Independent mathematical audit

## correctness

PASS

The complement involution (a,b)→(a^1,b^1) has precisely eight two-element input orbits. For each orbit its pair (c,d) of outputs must obey c∉{a,b}, d∉{bar a,bar b}, d≠bar c; different orbits are independent, with allowed list lengths [6,2,2,2,2,2,6,2]. The four mixed-color input-pair orbits contribute 4 C/G outputs, the fixed off-diagonal same-class orbits contribute 2, making baseline 6; the two diagonal-like orbits add 1/2 and 0/1. The exact product GF (2u²)(2)(2u)^4(4u+2u²)(2+4u)=512u^7+1280u^8+512u^9. The full 4-variable product of eight output monomials gives coefficient [x_0^4 x_1^4 x_2^4 x_3^4]=80. Enforcing transpose identifies the two mixed-orbit pairs and yields 16 simultaneously symbol-uniform/symmetric; 576 are symmetric without balance. Direct independent enumeration of all 6·2^5·6·2=2304 admissible tables, checking all 16 inequalities, reproduced GC 512/1280/512, uniform 80, symmetric 576, joint 16, and the displayed concrete 4×4 symmetric witness. This is an exhaustive finite proof because orbits partition the entire finite input domain, not a partial sample.

## originality

PASS

Choi arxiv:2603.27271 Theorem 10 and Definition 11 gives the same complement-sensitive self-synchronizing local marker constraints and one explicit F4 example, but does not state the complete GC histogram or output-uniform/transposed counts in inspected section. Published Resultary record 406f1f4dc0ca proves a broader unrestricted formula for number of admissible maps including unweighted total 2304; that number is acknowledged and does not determine the four-output symbol-frequency polynomial. Zhang–Wu 2025 concerns global DNA GC-balanced polar codes under different constraints, not local complement-table enumeration. The extra refined counts are natural constraints for local markers even though they may be elementary to compute from the earlier cycle/orbit argument; earlier refined generating functions under other terminology remain possible. No false downstream assertion of complete codeword-level GC balancing.

## value

PASS

Symbol balance and GC content are natural physical-design constraints for four-nucleotide local synchronization markers; knowing the total count of admissible maps does not indicate how many meet those constraints. The complete weighted spectrum and 16 joint symbol-uniform symmetric maps provide a directly usable, exhaustive lookup-table design classification and quantify a sharp ±1/16 GC bias under uniform flanks. This is a bounded but motivated complete finite theorem, not a claim of performance improvement for an entire DNA code.

The dated certificate retains the supplied scientific assessment, sources and limitations.
