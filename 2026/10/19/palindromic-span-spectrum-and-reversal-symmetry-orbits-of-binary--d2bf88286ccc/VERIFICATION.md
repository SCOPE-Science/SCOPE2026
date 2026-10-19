---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification of the palindrome-span spectrum

From the directory containing the four source files, execute:

```sh
python3 pal_cycle_dfs.py
g++ -std=c++17 -O2 pal_cycle_fsr.cpp -o pal_cycle_fsr
./pal_cycle_fsr
python3 pal_euler_n5.py
python3 pal_cycle_orbits.py
```

The independent Euler DFS and nonsingular feedback-register census both return `7:200 8:192 9:856 10:128 11:392 12:32 13:200 15:48`, totaling 2048 cycles. The feedback checker prints `FSR_VERIFY_OK`. The Euler-completion check reports zero extendible length-14 palindromes, six extendible length-15 palindromes, zero length-16 and zero length-17 palindromes, and prints `EULER_VERIFY_OK`. The complement/reversal orbit program prints:

```text
ORBIT length=7 size2=14 size4=43
ORBIT length=8 size2=4 size4=46
ORBIT length=9 size2=6 size4=211
ORBIT length=10 size2=0 size4=32
ORBIT length=11 size2=6 size4=95
ORBIT length=12 size2=0 size4=8
ORBIT length=13 size2=2 size4=49
ORBIT length=15 size2=0 size4=12
ORBIT_VERIFY_OK
```

The feedback iteration searches all 65536 possible pairing functions and checks each permutation orbit. The Euler DFS enumerates every possible cycle via distinct five-bit edges. The palindrome length bound follows independently from the finite Euler-completion test and the centered-subfactor argument. Each checker can be audited from its source; the count of passing tests alone is not the proof. No external proof assistant or independent audit is claimed. All verification claims concern the exact binary order-five domain only.
